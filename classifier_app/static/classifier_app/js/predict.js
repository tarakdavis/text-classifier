// put choices in dropdown

function onDropdown(response, $drop) {
    response.forEach(function(classif) {
        var $li = $('<li>').appendTo($drop)
        var $a = $('<a>').attr('href', '/classifier/' + classif.id).attr('id', classif.id).appendTo($li)
        var $p = $('<p>').text(classif.name).appendTo($a)
    })
}

function getClassifier(response) {
    return response.results.filter(function(result) {
      return result.id, result.name
    })
}

var $drop = $("#classchoice")
$.ajax({ url: '/api/classifier/' }).done(function(response) {
  onDropdown(getClassifier(response), $drop);
})


function onDropdown(response, $drop) {
    response.forEach(function(cat) {
        var $li = $('<li>').text(cat.name).appendTo($drop)

        // var $li = $('<li>').appendTo($drop)
        // var $p = $('<p>').text(cat.name).appendTo($li)
    })
}

function getCategory(response) {
    return response.results.filter(function(result) {
      return result.category
    })
}

var $drop = $("#catchoice")
$.ajax({ url: '/api/data/' }).done(function(response) {
  onDropdown(getCategory(response), $drop);
})


// get training data for a predict
$(document).ready(function(){
  $('#------').click(function(response){
// var $table = $("#answers")
    $.ajax({ url: '/api/predict/'}).done(function(response) {
      response.results.forEach(function(contents){
        if(contents.classifier == ###whatever classifier we are in ####){
          var $xtrain += contents.text
          var $ytrain += contents.category
        }
      })
    })
  })
 })

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
