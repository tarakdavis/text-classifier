// put choices in dropdown

<<<<<<< HEAD
function getClassifier(response) {
    return response.filter(function(result) {
      return result.name
    })
}

function onDropdown(response, $drop) {
    response.forEach(function(classif) {
        var x = document.getElementById("pickclassif");
        var optn = document.createElement("OPTION");
        optn.text = classif.name
        x.add(optn)
        return
    })
}




<<<<<<< HEAD

function onDropdown(response, $drop) {
    response.forEach(function(classif) {
        var $li = $('<li>').appendTo($drop);
        var $a = $('<a>').attr('href', '/classifier/' + classif.id).attr('id', classif.id).appendTo($li);
        var $p = $('<p>').text(classif.name).appendTo($a);
    });
}

function getClassifier(response) {
    return response.results.filter(function(result) {
      return result.id, result.name;
    });
}

var $drop = $("#classchoice");
>>>>>>> a6db236dcf4c9f7e0f7c190598dbad3fd2ad6a63
$.ajax({ url: '/api/classifier/' }).done(function(response) {
  onDropdown(getClassifier(response), $drop);
});

=======


// get training data for a predict
$(document).ready(function(){
  $('#------').click(function(response){
// var $table = $("#answers")
    var xtrain = {};
    $.ajax({ url: '/api/classifier/'}).done(function(response) {
      response.forEach(function(contents){
        if(contents.classifier == contents.user){
          var $xtrain += contents.text
          var $ytrain += contents.category
          (for var i = 0; i < contents.text.length(); i++){

          }
        }
      });
    });
  });
});

 // $(document).ready(function(){
 //   $('#------').click(function(response){
 //       var myKeyVals = {
 //           category: category,
 //           text: text,
 //           classif: classifier
 //       }
 //       $.ajax({
 //             type: 'GET',
 //             url: "/api/predict/",
 //             data: myKeyVals,
 //             success: function(data) { alert("Loading Complete") },
 //       })
 //   })
 // })
>>>>>>> a6db236dcf4c9f7e0f7c190598dbad3fd2ad6a63
