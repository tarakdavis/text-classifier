function onDropdown(response, $list) {
    response.forEach(function(data) {
        var $li = $('<p>').appendTo($list)
        var $a = $('<a>').attr('href', '/data_delete/' + data.id).attr('id', data.id).appendTo($li)
        var $p = $('<p>').text(data.category).appendTo($a)
        var $p = $('<p>').text(data.text).appendTo($a)

    })
}

function getBoards(response) {
    return response.filter(function(result) {
      return result.category, result.text
    })
}

var $list = $('#deleteList')
$.ajax({ url: '/api/data/' }).done(function(response) {
  onDropdown(getBoards(response), $list);
})
