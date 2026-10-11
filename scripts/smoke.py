import json,re,time
from pathlib import Path
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
from genlayer_py.contracts import actions as contract_actions
def compat(method=None,args=None,kwargs=None):
    out={}
    if method is not None: out["method"]=method
    if args: out["args"]=args
    if kwargs: out["kwargs"]=kwargs
    return out
contract_actions.make_calldata_object=compat
ROOT=Path(__file__).parents[1]; ENV=(ROOT.parents[3]/"accounts.env").read_text(encoding="utf-8")
KEY=re.search(r'^ACCOUNT_4_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)',ENV,re.M).group(1).strip()
ADDRESS=json.loads((ROOT/"deployment.json").read_text())["contractAddress"]
client=create_client(chain=studionet,account=create_account(account_private_key=KEY))
def write(name,args):
    tx=client.write_contract(address=ADDRESS,function_name=name,args=args); print(name+"_tx="+str(tx),flush=True)
    receipt=client.wait_for_transaction_receipt(transaction_hash=tx,wait_until="finalized",retries=180,interval=5000,full_transaction=True)
    leaders=receipt.get("consensus_data",{}).get("leader_receipt") or []; leaders=[leaders] if isinstance(leaders,dict) else leaders
    assert receipt.get("result_name")=="MAJORITY_AGREE" and any(x.get("execution_result")=="SUCCESS" for x in leaders)
    return str(tx)
edition_id="LIVE-EDITION-"+str(int(time.time()))
source=[{"id":"S1","text":"Participants may withdraw their consent at any time without affecting future care."},{"id":"S2","text":"The research team must explain urgent risks in plain language before enrollment."}]
translation=[{"id":"S1","text":"Les participants peuvent retirer leur consentement à tout moment sans affecter leurs soins futurs."},{"id":"S2","text":"L'équipe de recherche doit expliquer les risques urgents en langage clair avant l'inscription."}]
glossary=[{"source":"consent","target":"consentement"},{"source":"urgent risks","target":"risques urgents"}]
transactions={"pin":write("pin",[edition_id,"Research consent translation","English","French",json.dumps(source),json.dumps(translation),json.dumps(glossary)])}; transactions["align"]=write("align",[edition_id])
final=client.read_contract(address=ADDRESS,function_name="get_edition",args=[edition_id])
assert final["state"]=="ALIGNED" and final["band"] in ("FAITHFUL","USABLE","REVIEW") and len(final["alignment"])==2
proof={"editionId":edition_id,"contract":ADDRESS,"transactions":transactions,"final":final,"disclosure":"The source, translation and glossary are repository-owner demonstration text supplied directly to the contract."}
(ROOT/"evidence").mkdir(exist_ok=True); (ROOT/"evidence"/"live-run.json").write_text(json.dumps(proof,indent=2)+"\n",encoding="utf-8"); print(json.dumps(proof,indent=2))

