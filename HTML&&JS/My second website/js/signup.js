/**
 * Created by alex on 2016/8/28.
 */
(function(jq){

    function ErrorMessage(inp,message){
        console.log(message)
        var tag = document.createElement('span');
        tag.innerText = message;
        console.log(tag.innerText)
        inp.after(tag);
    }

    jq.extend({
        valid:function(form){
            // #form1 $('#form1')
            jq(form).find(':button').click(function(){
                console.log('button')
                jq(form).find('.item span').remove();

                var flag = true;
                jq(form).find(':text,:password').each(function(){

                    var require = $(this).attr('require');
                    if(require){
                        var val = $(this).val();
                        console.log(val)
                        if(val.length<=0){
                            var label = $(this).attr('label');
                            console.log(label)
                            ErrorMessage($(this),label+"不可以为空");
                            flag = false;
                            return false;
                        }

                        var minLen = $(this).attr('min-len');
                        if(minLen){
                            var minLenInt = parseInt(minLen);
                            if(val.length<minLenInt){
                                var label = $(this).attr('label');
                                ErrorMessage($(this),label + "长度最小为"+ minLen);
                                flag = false;
                                return false;
                            }
                            //json.stringify()
                            //JSON.parse()
                        }


                        var email = $(this).attr('email');
                        if(email){
                            // 用户输入内容是否是邮件格式
                            // var phoneReg = /^1[3|5|8]\d{9}$/;
                            var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

                            if(!re.test(val)){
                                var label = $(this).attr('label');
                                ErrorMessage($(this),label + "格式错误");
                                flag = false;
                                return false;
                            }
                        }



                        // 1、html自定义标签属性
                        // 增加验证规则+错误提示

                    }
                    // 每一个元素执行次匿名函数
                    // this
                    //console.log(this,$(this));
                    /*
                    var val = $(this).val();
                    if(val.length<=0){
                        var label = $(this).attr('label');
                        var tag = document.createElement('span');
                        tag.innerText = label + "不能为空";
                        $(this).after(tag);
                        flag = false;
                        return false;
                    }
                    */
                        //
                        // console.log($('#form-pwd').innerText)
                        // console.log($('#form-equalTopwd').innerText)
                        // if ($('#form-pwd').innerText!=null && $('#form-pwd').innerText!==$('#form-equalTopwd').innerText){
                        //     ErrorMessage($('#form-equalTopwd'),'密码不一样')
                        // }
                        // flag=false;
                        // return false


                });



                   if(flag==true){
                        var bt=document.getElementById('b1');
                        var username=document.getElementById('form-account');
                        var pwd=document.getElementById('form-pwd');
                        var pwd2=document.getElementById('form-equalTopwd');

                        if(pwd.value!==pwd2.value){
                                            jq(form).find('.item span').remove();

                            ErrorMessage(pwd2,'密码不一样')
                            flag=false
                            return false
                        }


                        if(username.value=='user' && pwd.value=='password' && pwd2.value==pwd.value){

                            alert("登录成功，跳转到登录界面")
                            location.href="login.html"
                            return false

                        }
                        else{
                                  alert("该用户已存在，注册失败")

                        }


                    }
                return flag;
            });
        }
    });
})(jQuery);
