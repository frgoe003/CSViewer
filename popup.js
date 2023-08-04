
// DOM References
import caseData from './caseData.json' assert {type: 'json'};
import caseData2 from './caseData.js'
let caseData3 = caseData2[0]

let pullBtn = document.getElementById('pull');
let testBtn = document.getElementById('test');
let caseTable = document.getElementById('table');


pullBtn.addEventListener("click", async () => {
  main();
});
testBtn.addEventListener("click", async () => {
  console.log(caseData3)
  console.log(caseData3['MP5-SD'])
  console.log(caseData3['MP5-SD']['Liquidation'])
});
function main(){
  getHeader()

}


