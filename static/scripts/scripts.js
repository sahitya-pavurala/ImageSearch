$(document).on('submit', '#search-form', function(event){
    event.preventDefault();
    $.ajax({
      url: "/search?keyword=" + $("#search").val(),
      success: function(response){
        $("#results").html(response);
      },
      error: function(error){
        $("#results").html('<div class="row">No results found.</div>');
      }
    });
});