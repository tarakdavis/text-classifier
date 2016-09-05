$(document).ready(function(){
    $('#newStuff').click(function(){
        var clName = $('#inputclass').val()
        var catName = $('#inputcat').val()
        var theText = $('#textArea').val()

        function getClassifiers(response) {
            return response.filter(function(result) {
              return result.name
            })
        }

        function checkIfAlreadyExist(response, clName) {
            var $flag = "NO"
            response.forEach(function(check){
                if (check.name == clName){ $flag = "YES" }
                })

            if ($flag == "NO" ){
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
            }

        $.ajax({ url: '/api/classifier/' }).done(function(response) {
          checkIfAlreadyExist(getClassifiers(response), clName);
            });


        $temp = $.ajax({ url: '/api/classifier/' }).done(function(response) {
          $lastID = (response.length)+1
          var myKeyVals = {
            category: catName,
            text: theText,
            classifier: $lastID
          }
          console.log(myKeyVals)
          $temp = $.ajax({
              type: "POST",
              url: "/api/data/",
              data: myKeyVals,
              contentType: "application/json; charset=utf-8",
              dataType: "json",
              success: function() { alert("Data Save Complete")
                    window.location='/'}
            })
      })
    })
})
