chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    var currentURL = tabs[0].url;
    console.log(currentURL);
    if (currentURL.includes('youtube.com')) {
        var url = new URL(currentURL);
        var pathname = url.pathname;

        //seperate the url 
        var urlArray = pathname.split('/');
        var videoID = urlArray[2];

        try{
            psuedoCode
        }
        catch(error){
            console.log("error", error);
        }
        
    } else 
        console.log('This is not a youtube website website.');
}
);

