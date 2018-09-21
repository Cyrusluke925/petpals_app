

$.ajax({
    method: 'Get',
    url: '/api/posts',
    success: function onSuccess(e) {
        console.log(e.posts)
    }
})

// console.log('hello')
console.log('cya')
$('.postLike').on('click', function(element){
    $(this).css('color', 'red')
    element.preventDefault();
    var form = $('.likeform').serialize()
    var post = $(this).attr('value')
    var user = $('.user').attr('value')
    console.log(post)
    console.log(user)
    var theData = {
        post: post,
        user: user,
        form: form
    }

    likeURL = `http://localhost:8000/post/${post}/like`
    console.log("URL: ", likeURL)
    $.ajax({
        method: 'POST',
        url:likeURL,
        data: theData,
        success: function onSuccess(e) {
            console.log(e);
            // $(this).css('color', 'red')
        },
        error: function onError(err1, err2, err3) {
            console.log(err)

        }
        

    })
    
})








