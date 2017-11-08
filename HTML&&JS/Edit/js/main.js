/**
 * Created by yuan.li on 6/9/2017.
 */

//全选
function checkAll() {
    $(':checkbox').prop('checked', true).change()
}

//取消
function cancelAll() {
    $(':checkbox').prop('checked', false).change()
}

//反选
function reversAll() {
    $(':checkbox').each(function () {
        var flag = $(this).prop('checked') ? false : true;
        $(this).prop('checked', flag).change()
    })
}


//当checkbox状态改变的时候触发事件

$("#tb").delegate(":checkbox", "change", function () {

    if ($('#edit').attr('name') == 'true') {

        //如果是在编辑模式下勾住了，那么激活他后面的标签，IP和Port的cell格子上面添加一个相同尺寸的文本框，下拉框解锁

        $(':checkbox').each(function () {

            //打钩的处理
            if ($(this).prop('checked')) {
                var c = $(this);

                if ($(this).attr('flag') == 'true') {
                    console.log('no change')
                }
                else {

                    $(this).attr('flag', 'true');

                    //解锁状态栏下拉框
                    var v = $(this).parent().nextAll()[2]
                    $(v).children().removeAttr('disabled')


                    //IP和port上添加一个文本框进行编辑
                    $(this).parent().nextAll().slice(0, 2).each(function () {
                        var tmp = $(this).text();
                        console.log(tmp);
                        $(this).html('<input type="text" name= "input" value="' + tmp + '"/>')

                    })


                }
            }

            //取消打钩的处理
            else {

                $(this).removeAttr('flag');

                //锁住状态框
                var v = $(this).parent().nextAll()[2]
                $(v).children().attr('disabled', true)

                //IP和port回写内容到表格里面
                $(this).parent().nextAll().slice(0, 2).each(function () {
                    var temp = $(this).children().val();
                    $(this).html(temp);
                    $(this).children().remove()

                })

            }

        })
    }
})


//点击编辑框的事件
$('#edit').click(function () {
    //进入编辑状态
    if ($(this).attr('name') == 'false') {

        $(":button").removeAttr('disabled');
        $(":checkbox").removeAttr('disabled');

        $(this).attr('name', 'true');
        $(this).css('background-color', '#FFFF00');

          $(':checkbox').each(function () {

            //打钩的处理
            if ($(this).prop('checked')) {
                var c = $(this);

                if ($(this).attr('flag') == 'true') {
                    console.log('no change')
                }
                else {

                    $(this).attr('flag', 'true');

                    //解锁状态栏下拉框
                    var v = $(this).parent().nextAll()[2]
                    $(v).children().removeAttr('disabled')


                    //IP和port上添加一个文本框进行编辑
                    $(this).parent().nextAll().slice(0, 2).each(function () {
                        var tmp = $(this).text();
                        console.log(tmp);
                        $(this).html('<input type="text" name= "input" value="' + tmp + '"/>')

                    })


                }
            }

            //取消打钩的处理


        })


    }
    //离开编辑状态
    else {
        $("select").attr('disabled', true)
        $(this).attr('name', 'false');
        $(this).css('background-color', '');
        $(':checkbox').removeAttr('flag');

        // $(":checkbox").attr('disabled', true);
        $(":checkbox").attr('checked', false);


        if ($('input[name="input"]')) {
            $('input[name="input"]').each(function () {
                console.log($(this));
                $(this).parent().html($(this).val())

            })
        }
    }
})