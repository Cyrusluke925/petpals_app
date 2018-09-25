$.ajax({
    method: 'Get',
    url: '/api/posts',
    success: function onSuccess(e) {
        console.log(e.posts)
    }
})

$('.postLike').on('click', function(element){
    element.preventDefault();
    $(this).addClass('fullHeart')

    var form = $('.likeform').serialize()
    var post = $(this).attr('value')
    var user = $('.user').attr('value')

    console.log("post liked:", post)
    console.log("by user according to form:",user)
    
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
        success: function onSuccess(json) {
                console.log(json)
                likesCount =json.likes.length
                if (likesCount > 0) {
                    $('.likeform p').text(`likes: ${likesCount}`)
                }
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

$('#commentBox').on('submit',(e)=>{
    e.preventDefault()
})

$('.delete').on('click',(e)=>{
    e.preventDefault()
    $.ajax({
        method: 'DELETE',
        url:'/feed',
        success: function onSuccess(e) {
            console.log('success')
        },
        error: function onError(err) {
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

$('.profile_post_box img').hover(
    function() {
    $(this).css('opacity', '.3')  
    $(this).siblings().fadeIn(500).hover (
        function () {
            $(this).show();
            $(this).siblings().css('opacity', '.3') 
        }
    )
    }, function () {
        $('.profile_post_box img').css('opacity', '1')  
        $('.profile_post_box img').siblings().hide()
    }
);