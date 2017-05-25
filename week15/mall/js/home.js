var doc = document;
//中间轮播图，定时自动切换、点击箭头切换、点击圆点切换、鼠标悬浮时停止自动轮播和鼠标离开时开始自动轮播
var changimg = function () {
    var imglist = doc.getElementById("imgs"),
        imgs = imglist.getElementsByTagName("li"),
        circlelist = doc.getElementById("circles"),
        circles = circlelist.getElementsByTagName("li"),
        len = imgs.length,
        imgwidth = imgs[0].offsetWidth,
        totalwidth = imgwidth * (len - 1) * (-1),
        varywidth = imglist.offsetLeft,
        i = 0,
        timer;
    //下一张图片(不能实现无缝轮播，因为使用transition有过渡时间，不能瞬间切换图片)
    function nextimg() {
        if (varywidth > totalwidth) {
            varywidth -= imgwidth;
            circles[i].className = "circle";
           // console.log(circles[i]);
            i++;
        }
        else {
            varywidth = 0;
            circles[len - 1].className = "circle";
            // console.log(circles[i]);
            i = 0;
        }
        imglist.style.left = varywidth + "px";
        circles[i].className = "currimg";
    }

    //上一张图片
    function previmg() {
        if (varywidth < 0) {
            varywidth += imgwidth;
            circles[i].className = "circle";
            i--;
        }
        else {
            varywidth = totalwidth;
            circles[0].className = "circle";
            i = len - 1;
        }
        imglist.style.left = varywidth + "px";
        circles[i].className = "currimg";
    }

    //点击圆点切换图片
    function dotimg(event) {
        var e = event || window.event,
            target = e.target || e.srcElement,
            num;
        if(target.tagName.toLowerCase()==="li"){
            num = parseInt(target.getAttribute("data-num"));
            varywidth = imgwidth * num * (-1);
            imglist.style.left = varywidth + "px";
            for (var j = 0; j < len; j++) {
                circles[j].className = "circle";
            }
            target.className = "currimg";
            i = num;
        }

    }

    //开启自动切换
    function startAutochange() {
        timer = setInterval(nextimg, 3000);
    }

    //停止自动切换
    function stopAutochange() {
        clearInterval(timer);
    }

    return {
        nextimg: nextimg,
        previmg: previmg,
        dotclick: dotimg,
        startauto: startAutochange,
        stopauto: stopAutochange
    }
}();
//右侧切换选项卡显示不同的内容
var tabs = function () {
    var tabs = doc.getElementsByClassName("tab"),
        tabctns = doc.getElementsByClassName("tabctn"),
        len = tabs.length;
//切换选项卡显示不同的内容
    function tabschange(event) {
        var e = event || window.event,
            target = e.target || e.srcElement;
        if (target.tagName.toLowerCase() === "a") {
            for (var i = 0; i < len; i++) {
                if(i===len-1){
                    tabs[i].className = "tab";
                }
                else{
                    tabs[i].className = "tab border";
                }
                tabctns[i].className = "tabctn";
            }
            target.className += " activelink";
            target.nextElementSibling.className += " active";
        }

    }

    return {
        tabchange: tabschange
    }
}();
//底部自动轮播图，鼠标悬浮和离开时分别停止和启动自动轮播，点击小图显示大图。
//var bottomimg = function () {
//     var elem = doc.getElementById("showgoods"),
//         goodlist = elem.getElementsByTagName("ul")[0],
//         goods = elem.getElementsByTagName("li"),
//         len = goods.length,
//         imgwidth = goods[0].offsetWidth,
//         totalwidth = imgwidth * (len - 7) * (-1),
//         speed = 2,
//         currleft = 0,
//         timer,
//         bigimg = doc.getElementById("bigimg");
//     function bottomimg() {
//         if (currleft < totalwidth) {
//             currleft = 0;
//         }
//         currleft -= speed;
//         goodlist.style.left = currleft + "px";
//     }
//
//     //开启自动切换
//     function startAutochange() {
//         timer = setInterval(bottomimg, 30);
//     }
//
//     //停止自动切换
//     function stopAutochange() {
//         clearInterval(timer);
//     }
//     return {
//         turnimg: bottomimg,
//         startauto: startAutochange,
//         stopauto: stopAutochange,
//     }
// }();
//搜索框表单验证
function validateForm() {
    var search = doc.getElementById("select").value;
    if (search === "" || search === null) {
        alert("请输入搜索文字！");
        return false;
    }
    else {
        alert("进行查询！");
    }
}




window.onload = function () {
    //启动定时轮播图片
    console.log("change")
    changimg.startauto();
    //bottomimg.startauto();




};
//点击右箭头切换到下一张图片
doc.getElementById("arrR").addEventListener("click", changimg.nextimg, false);
//点击左箭头切换到上一张图片
doc.getElementById("arrL").addEventListener("click", changimg.previmg, false);
//点击圆点切换对应图片
doc.getElementById("circles").addEventListener("click", changimg.dotclick, false);
//鼠标悬浮图片上时停止自动轮播
//doc.getElementById("turnimg").addEventListener("mouseover", changimg.stopauto, false);
//鼠标离开图片时自动轮播
doc.getElementById("turnimg").addEventListener("mouseout", changimg.startauto, false);
//鼠标悬浮列表项上时切换至对应选项卡
//doc.getElementById("tabs").addEventListener("mouseover", tabs.tabchange, false);
//鼠标悬浮图片上时停止自动轮播
//doc.getElementById("showgoods").addEventListener("mouseover", bottomimg.stopauto, false);
//鼠标离开图片时自动轮播
//doc.getElementById("showgoods").addEventListener("mouseout", bottomimg.startauto, false);
//验证搜索框内容是否为空
//oc.getElementById("btnquery").addEventListener("click", validateForm, false);

window.onload = function(){
    var goods = document.getElementsByClassName('goods')[0];
    // 用于保存购物车商品信息
    var carList = [];
    // 先获取当前cookie
    console.log('reading cookie')
    var cookies = document.cookie.split('; ');
    console.log(cookies)
    for(var i=0;i<cookies.length;i++){
        var arr = cookies[i].split('=');
        if(arr[0] === 'carlist'){
            carList = JSON.parse(arr[1]);
        }
        if(arr[0]=='accountInfo'){
            console.log('Login'+arr[1])
            if(arr[1]!=='xx'){
                var s1=document.getElementById('d1');
                var s2=document.getElementById('d2');
                var s3=document.getElementById('l1');
                var s4=document.getElementById('l2');
                s1.style.display='None';
                s2.style.display='block'
                s3.style.display='None';
                s4.style.display='block';
            }

        }

    }

     var num=document.getElementById('itemNum');
        num.innerHTML=carList.length;

// 事件委托
    goods.onclick = function(e){
        //兼容旧版IE
        e = e || window.event;
        var target = e.target || e.srcElement;
        // 添加到购物车
        if(target.tagName.toLowerCase() === 'button'){
        // 获取当前li （Li-div-button)
        var currentLi = target.parentElement.parentElement;
        var children = currentLi.children;
        var currentGUID = currentLi.getAttribute('data-guid');
        // 先创建一个对象保存当前商品信息
        var goodsObj = {};
        goodsObj.guid = currentGUID;
        goodsObj.qty = 1;
        goodsObj.name = children[1].innerHTML;
        goodsObj.price = children[2].innerHTML;
        goodsObj.imgUrl = children[0].src;
        // 如果cookie为空，则直接添加
        if(carList.length===0){
        // 添加到carList
        carList.push(goodsObj);
        }else{
        // 先判断cookie中有无相同的guid商品
            for(var i=0;i<carList.length;i++){
            // 如果商品已经存在cookie中，则数量+1
                if(carList[i].guid === currentGUID){
                    carList[i].qty++;
                    break;
                }
            }
    // 如果原cookie中没有当前商品
        if(i===carList.length){
        // 添加到carList
        carList.push(goodsObj);
        }

        }
        // 存入cookie
        // 把对象/数组转换诚json字符串：JSON.stringify()
        document.cookie = 'carlist=' + JSON.stringify(carList);
        document.cookie ="path=/;"
        }

        var num=document.getElementById('itemNum');
        num.innerHTML=carList.length;

    }










}