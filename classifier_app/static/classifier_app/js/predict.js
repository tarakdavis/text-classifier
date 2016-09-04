

============================== CLASSIFIER CHOICES ===================================

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
var $drop = $('#pickclassif')
$.ajax({ url: '/api/classifier/' }).done(function(response) {
  onDropdown(getClassifier(response), $drop);
});



=======
var $drop = $("#classchoice");


============================== CATEGORY CHOICE ===================================


function onDropdown(response, $drop) {
    response.forEach(function(cat) {
        var $li = $('<li>').text(cat.name).appendTo($drop);

        // var $li = $('<li>').appendTo($drop)
        // var $p = $('<p>').text(cat.name).appendTo($li)
    });

function getCategory(response) {
    return response.results.filter(function(result) {
      return result.category;
    });
}

var $drop = $("#catchoice");
$.ajax({ url: '/api/data/' }).done(function(response) {
  onDropdown(getCategory(response), $drop);
});



============================== COOKIES ===================================

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;


var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
