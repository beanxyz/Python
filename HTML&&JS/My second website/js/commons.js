/**
 * Created by alex on 2016/8/28.
 */
(function(jq){

    function ErrorMessage(inp,message){
        var tag = document.createElement('span');
        tag.innerText = message;
        inp.after(tag);
    }

    jq.extend({
        valid:function(form){
            // #form1 $('#form1')
            jq(form).find(':button').click(function(){

                jq(form).find('.item span').remove();

                var flag = true;
                jq(form).find(':text,:password').each(function(){

                    var require = $(this).attr('require');
                    if(require){
                        var val = $(this).val();

                        if(val.length<=0){
                            var label = $(this).attr('label');
                            ErrorMessage($(this),label + "不能为空");
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

                        var phone = $(this).attr('phone');
                        if(phone){
                            // 用户输入内容是否是手机格式
                            var phoneReg = /^1[3|5|8]\d{9}$/;
                            if(!phoneReg.test(val)){
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




                });
                   if(flag==true){
                        var bt=document.getElementById('b1');
                        var username=document.getElementById('username');
                        var pwd=document.getElementById('pwd');

                        if(username.value=='user' && pwd.value=='password'){
                            var login={};
                            login.username='user';
                            login.pwd='password'
                            console.log(login)
                            var info=JSON.stringify(login);
                            document.cookie="accountInfo="+info;
                            alert("登录成功，跳转到登录界面")
                            location.href="index.html"

                        }
                        else{
                                  alert("登录失败")

                        }


                    }
                return flag;
            });
        }
    });
})(jQuery);
