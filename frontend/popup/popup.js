chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    var currentURL = tabs[0].url;
    console.log(currentURL);
    if (currentURL.includes('leetcode.com')) {
        var url = new URL(currentURL);
        var pathname = url.pathname;
        var parts = pathname.split('/');
        var questionName = parts[parts.length - 2];


        try{
            psuedoCode
        }
        catch(error){
            console.log("error", error);
        }
        
    } else 
        console.log('This is not a leetcode website.');
}
);

