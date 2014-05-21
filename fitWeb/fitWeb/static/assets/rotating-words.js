	(function(){
    var words = [
		'SMART',
        'COOL',
        'CLEAN'
        ], i = 0;
    setInterval(function(){
        $('#word-change').slideUp(function(){
            $(this).html(words[i=(i+1)%words.length]).slideDown();
        });
    }, 1000);
        
})();