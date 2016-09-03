var $submitData = $('#submitData');
var $textValue = $('#textValue');
var $categoryValue = $('#categoryValue');
var $classifierValue = $('#classifierValue');




$addDataForm.submit(function() {
$.ajax({
        type: 'POST',
        url: "/api/data/",
        data: {
          category: $categoryValue.val(),
          text: $textValue.val(),
          classifier: $classifierValue.val(),
        },
        dataType: "text",
  });
});
