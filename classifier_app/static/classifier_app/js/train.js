$(document).ready(function(){
    $('#newStuff').click(function(){
        var clName = $('#inputclass').val()
        var catName = $('#inputcat').val()
        var theText = $('#textArea').val()
        console.log(catName, theText)
        $.ajax({
            type: 'POST',
            url: "/api/classifier/",
            data: {name: clName},
            success: function() { alert("Classifer Save Complete") },
        })

        $temp = $.ajax({ url: '/api/classifier/' }).done(function(response) {
                  $lastID = (response.length)+1
                  var myKeyVals = {
                    category: catName,
                    text: theText,
                    classifier: $lastID
                  }
                  $.ajax({
                      type: 'POST',
                      url: '/api/data/',
                      data: myKeyVals,
                      success: function() { alert("Data Save Complete")
                            window.location='/'
                        },
                  })
            })
        })
})
