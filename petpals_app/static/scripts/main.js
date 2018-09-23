// $("a.like").click(function(){
//     var curr_elem = $(this) ;
//     $.get($(this).attr('href'), function(data){
//         var my_div = $(curr_elem).parent().find("b");
//         my_div.text(my_div.text()*1+1);     
//     }); 
//     return false; // prevent loading URL from href
// });

$(document).ready(function() {

    var user = $('.user').attr('value')
    console.log(user)

    $.ajax({
        method: 'Get',
        url: '/api/likes',
        data: user,
        success: function handleSuccess (json) {
            console.log(json.likes)
            console.log('logged in:',user)
            let likesArray = json.likes

            new_array = []
            $.each(likesArray, function () {
                if (user == this.user) {
                    console.log('there is a like for this user in the db')
                    console.log(this.post)
                    new_array.push(this.post)
                }
            });
            console.log("array of logged in users likes:",new_array)

            $.ajax({
                method: 'Get',
                url: '/api/feed',
                data: user,
                success: function handleSuccess (json) {
                    let postArray = json.posts
                    // console.log(postArray)
                    new_post_array = []
                    $.each(postArray, function () {
                        new_post_array.push(this.post)
                    });
                    console.log('array of logged in users feed posts:',new_post_array)
                    
                   

                    var matches = new_post_array.filter(function(val) {
                        return new_array.indexOf(val) != -1;
                    });
                
                    console.log(matches)
                }
            });
        }
        });
    });



function overlap(arr1,arr2) {
    for(var i = 0; i < new_array.length; ++i)
    if(new_post_array.indexOf(new_array[i]) != -1)
        return true;
    return false;
}
                            // $.each(postArray, function () {
                                // if (post == )
                        
                    // });
                    // if (post == )
                // }
                
    //         });
    //     }
    // });

//                     // console.log ($('.postLike').attr('value') )
//                     // let post = this.post
//                     // console.log(post)
//                     // $('.postLike').attr('value', post) 
//                     // console.log ( $('.postLike').attr('value'))
//                     // $('.postLike').css('color', 'red')
//                 }
//             })
//         },
//         error: function handleError (e){
//             console.log('error', e);
//         }
// });

$.ajax({
    method: 'Get',
    url: '/api/posts',
    success: function onSuccess(e) {
        console.log(e.posts)
    }
})

$('.postLike').on('click', function(element){
    element.preventDefault();
    $(this).css('color', 'red')

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
        success: function onSuccess() {
                console.log('success')
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
