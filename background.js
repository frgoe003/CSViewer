
function register(lessonId){
  //json = getRequest(lessonId);

  POSTrequest = {
    'lessonId':lessonId,
  }

  fetch('http://localhost:8000', {
       'method': 'POST',  
       'mode': 'cors',
       'headers': {
        'Content-Type': 'application/json'
      },
      'body': JSON.stringify(POSTrequest)
     }).then(res => {
      json = res.json();
      console.log(json);
    })
     .catch((error) => {
      console.log('This is Error message -', error);
    });
}



// inital read of authorization key
function deregister(lessonId){
  
}



////////////////////////
// CHROME MESSAGE API //
////////////////////////

chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {

    console.log(request.lessonId);
    register(request.lessonId);
    sendResponse({farewell: 'Registration request saved!'});  
  }
  
);


// on installed, check login
chrome.runtime.onInstalled.addListener(function(details){
  if(details.reason == 'install'){
      console.log('This is a first install!');
  }else if(details.reason == 'update'){
      var thisVersion = chrome.runtime.getManifest().version;
      console.log('Updated from ' + details.previousVersion + ' to ' + thisVersion + '!');
  }
  //window.open('https://schalter.asvz.ch/tn/account/user-data', '_blank')



});
