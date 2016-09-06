$(document).ready(function(){
    $('#newStuff').click(function(){
        var clName = $('#inputclass').val()
        var catName = $('#inputcat').val()
        var theText = $('#textArea').val()
        var $flag = "NEW"

        function getClassifiers(response) {
            return response.filter(function(result) {
              return result.name
            })
        }

        function checkIfAlreadyExist(response, clName, $flag) {
            response.forEach(function(check){
                if (check.name == clName){ $flag = String(check.id) }
                })
            if ($flag == "NEW" ){
                $.ajax({
                    type: 'POST',
                    url: "/api/classifier/",
                    data: {name: clName},
                    success: function() { alert("Classifer Save Complete") },
                        })
            }
            else {
                alert ("Classifier is already in your database.")
                    }
            var myKeyVals = {
                category: catName,
                text: theText,
                classifier: $flag
                }
            $.ajax({
                  type: "POST",
                  url: "/api/data/",
                  data: myKeyVals,
                  success: function() { alert("Data Save Complete")
                        window.location='/'}
                })
            }

        $.ajax({ url: '/api/classifier/' }).done(function(response) {
          checkIfAlreadyExist(getClassifiers(response), clName, $flag);
            });
    })
})
