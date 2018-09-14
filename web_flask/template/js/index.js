$(function () {
    var $button = $(".button");
    var $word = $(".input");
    var $box = $(".box2");

    $button.click(function () {
        var woline = $word.val();
        $newLine = $('<div class="every-line"><span class="thing">' + woline + '</span><div class="change"><a href="#">删除</a><a href="#">↑</a><a href="#">↓</a><a href="#">编辑</a></div></div>')
        if (woline == '') {
            alert("内容不能为空")
        }else{
            $box.append($newLine)
            $word.val("")
        }
    })

    $box.delegate("a","click",function () {
        var $every_line = $(this).parent().parent();
        $shangline = $(this).parent().prev()

        // case 是入口的意思，break是停止执行的意思，如果没有break，则会继续执行下面的case
        switch ($(this).text()) {
            case "删除":
                $every_line.remove();
                break;

            case "↑":
                if ($every_line.prev().text() == "") {
                    alert("已经到顶部啦");
                }else{
                    $every_line.insertBefore($every_line.prev());
                }
                break;

            case "↓":
                if ($every_line.next().text() == "") {
                    alert("已经到底部啦");
                }else{
                    $every_line.insertAfter($every_line.next());
                }
                break;

            case "编辑":
                $(".box3").show();
                $(".box3").find(".second-line input").val($(this).parent().prev().text());
                break;

            default:
                break;
        }
    })

    $(".x,.btx").click(function () {
        $(".box3").hide();
    })

    $(".btq").click(function () {
        $shangline.text($(".box3").find(".second-line input").val());
        $(".box3").hide();
    })
})








// if ($(this).text()=="删除") {
//     $every_line.remove();

// }else if ($(this).text()=="↑") {
//     if ($every_line.prev().text() == "") {
//         alert("已经到顶部啦");
//     }else{
//         $every_line.insertBefore($every_line.prev());
//     }

// }else if ($(this).text()=="↓") {
//     if ($every_line.next().text() == "") {
//         alert("已经到底部啦");
//     }else{
//         $every_line.insertAfter($every_line.next());
//     }

// }else if ($(this).text()=="编辑") {
//     $(".box3").show();
//     $(".box3").find(".second-line input").val($(this).parent().prev().text());

//     $(".btq").click(function () {

//         $shangline.text($(".box3").find(".second-line input").val());

//         $(".box3").hide();
//         return false
//     })
//         return false
// }