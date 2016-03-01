/**
 * Created by brianthomas on 3/1/16.
 */

$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/moneykatz/like_category/', {category_id: catid}, function(data){
        $('#like_count').html(data);
        $('#likes').hide();
    });
});