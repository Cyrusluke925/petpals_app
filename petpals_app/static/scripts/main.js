// $(document).ready(function() {
//     var user = $('.user').attr('value')
//     console.log(user)

//     $.ajax({
//         method: 'Get',
//         url: '/api/likes',
//         data: user,
//         success: function handleSuccess (json) {
//             console.log(json.likes)
//             console.log(user)
//             let likesArray = json.likes
            
//             $.each(likesArray, function () {
//                 if (user == this.user) {
//                     console.log('exists')
//                     // console.log ($('.postLike').attr('value') )
//                     let post = this.post
//                     console.log(post)
//                     // $('.postLike').attr('value', post) 
//                     // console.log ( $('.postLike').attr('value'))
//                     $('.postLike').css('color', 'red')
//                 }
//             })
//         },
//         error: function handleError (e){
//               console.log('error', e);
//          })
// });

$.ajax({
    method: 'Get',
    url: '/api/posts',
    success: function onSuccess(e) {
        console.log(e.posts)
    }
})

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

$('.follow').on('click', function(element){
    $(this).text('Following')
    element.preventDefault();

    var form = $('.followform').serialize()
    var user_to = $(this).attr('value')
    var user_from = $('.userFrom').attr('value')
    console.log(user_to)
    console.log(user_from)
    var theData = {
        user_to: user_to,
        user_from: user_from,
        form: form
    }

    followURL = `http://localhost:8000/user/${user_to}/follow`

    $.ajax({
        method: 'POST',
        url:followURL,
        data: theData,
        success: function onSuccess(e) {
            console.log('success')
        },
        error: function onError(err1, err2, err3) {
            console.log(err)
        }
    })  
})

$('.exploreBox img').hover(
    function() {
    $(this).css('opacity', '.3')  
    $(this).siblings().fadeIn(500).hover (
        function () {
            $(this).show();
            $(this).siblings().css('opacity', '.3') 
        }
    )
    }, function () {
        $('.exploreBox img').css('opacity', '1')  
        $('.exploreBox img').siblings().hide()
    }
);
