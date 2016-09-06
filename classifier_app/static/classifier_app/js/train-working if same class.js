$(document).ready(function(){
    $('#newStuff').click(function(){
        var clName = $('#inputclass').val()
        var catName = $('#inputcat').val()
        var theText = $('#textArea').val()
        var $flag = "NEW"
        var $clKey = ""

        function getClassifiers(response) {
            return response.filter(function(result) {
              return result.name
            })
        }

        function checkIfAlreadyExist(response, clName, $flag, $clKey) {
            response.forEach(function(check){
                if (check.name == clName){
                    $flag = "classifierALREADYexists"
                    $clKey = String(check.id)
                    }
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

            function checkAgain(response, clName, $clKey) {
                response.forEach(function(check){
                    if (check.name == clName){
                        $clKey = String(check.id)
                        }
                    })
                    var myKeyVals = {
                        category: catName,
                        text: theText,
                        classifier: $clKey
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
              checkAgain(getClassifiers(response), clName, $clKey);
                });
            }

        $.ajax({ url: '/api/classifier/' }).done(function(response) {
          checkIfAlreadyExist(getClassifiers(response), clName, $flag, $clKey);
            });
    })

// The event listener for the file upload
document.getElementById('fileSelect').addEventListener('change', upload, false);

// Method that checks that the browser supports the HTML5 File API
function browserSupportFileUpload() {
    var isCompatible = false;
    if (window.File && window.FileReader && window.FileList && window.Blob) {
    isCompatible = true;
    }
    return isCompatible;
}

// Method that reads and processes the selected file
function upload(evt) {
if (!browserSupportFileUpload()) {
    alert('The File APIs are not fully supported in this browser!');
    } else {
        var data = null;
        var file = evt.target.files[0];
        var reader = new FileReader();
        reader.readAsText(file);
        reader.onload = function(event) {
            var csvData = event.target.result;
            data = csvData;
            if (data && data.length > 0) {
              alert('Imported -' + data.length + '- rows successfully!');
              document.getElementById("textArea").value += data;
            } else {
                alert('No data to import!');
            }
        };
        reader.onerror = function() {
            alert('Unable to read ' + file.fileName);
            };
        }
    }
})
