function buildCatList(response, $list) {
    response.forEach(function(data) {
        var $li = $('<p>').appendTo($list)
        var $a = $('<a>').attr('href', '/data_delete/' + data.id).attr('id', data.id).appendTo($li)
        var $p = $('<p>').text(data.category).appendTo($a)
        // var $p = $('<p>').text(data.text).appendTo($a)

    })
}

function getCategories(response) {
    return response.filter(function(result) {
      return result.category, result.text
    })
}

var $list = $('#deleteList')
$.ajax({ url: '/api/data/' }).done(function(response) {
  buildCatList(getCategories(response), $list);
})

// =========================================================================

function buildClsList(response, $Clsfrlist) {
    response.forEach(function(classifier) {
        var $li = $('<p>').appendTo($Clsfrlist)
        var $a = $('<a>').attr('href', '/classifier_delete/' + classifier.id).attr('id', classifier.id).appendTo($li)
        var $p = $('<p>').text(classifier.name).appendTo($a)

    })
}

function getClassifiers(response) {
    return response.filter(function(result) {
      return result.name
    })
}

var $Clsfrlist = $('#deleteClsfrList')
$.ajax({ url: '/api/classifier/' }).done(function(response) {
  buildClsList(getClassifiers(response), $Clsfrlist);
})
