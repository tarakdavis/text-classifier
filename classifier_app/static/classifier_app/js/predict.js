// put choices in dropdown

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
})


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
}
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
