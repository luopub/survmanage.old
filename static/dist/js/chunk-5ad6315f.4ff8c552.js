(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-5ad6315f"],{1938:function(t,e,a){"use strict";a("4f58")},"36bd":function(t,e,a){"use strict";var n=a("4bf8"),i=a("77f1"),o=a("9def");t.exports=function(t){var e=n(this),a=o(e.length),r=arguments.length,s=i(r>1?arguments[1]:void 0,a),u=r>2?arguments[2]:void 0,c=void 0===u?a:i(u,a);while(c>s)e[s++]=t;return e}},"386d":function(t,e,a){"use strict";var n=a("cb7c"),i=a("83a1"),o=a("5f1b");a("214f")("search",1,(function(t,e,a,r){return[function(a){var n=t(this),i=void 0==a?void 0:a[e];return void 0!==i?i.call(a,n):new RegExp(a)[e](String(n))},function(t){var e=r(a,t,this);if(e.done)return e.value;var s=n(t),u=String(this),c=s.lastIndex;i(c,0)||(s.lastIndex=0);var l=o(s,u);return i(s.lastIndex,c)||(s.lastIndex=c),null===l?-1:l.index}]}))},"3b2b":function(t,e,a){var n=a("7726"),i=a("5dbc"),o=a("86cc").f,r=a("9093").f,s=a("aae3"),u=a("0bfb"),c=n.RegExp,l=c,d=c.prototype,h=/a/g,m=/a/g,f=new c(h)!==h;if(a("9e1e")&&(!f||a("79e5")((function(){return m[a("2b4c")("match")]=!1,c(h)!=h||c(m)==m||"/a/i"!=c(h,"i")})))){c=function(t,e){var a=this instanceof c,n=s(t),o=void 0===e;return!a&&n&&t.constructor===c&&o?t:i(f?new l(n&&!o?t.source:t,e):l((n=t instanceof c)?t.source:t,n&&o?u.call(t):e),a?this:d,c)};for(var g=function(t){t in c||o(c,t,{configurable:!0,get:function(){return l[t]},set:function(e){l[t]=e}})},y=r(l),v=0;y.length>v;)g(y[v++]);d.constructor=c,c.prototype=d,a("2aba")(n,"RegExp",c)}a("7a56")("RegExp")},4865:function(t,e,a){"use strict";var n=function(){var t=this,e=t._self._c;return e("div",{staticClass:"w-100 roi-preview-image",attrs:{id:"roiImageBox"}},[e("img",{class:t.roiImgClass,attrs:{id:t.roiImageId,src:t.imgSrc,alt:"工地当前图片"}}),e("canvas",{class:t.roiCanvasClass,attrs:{id:t.canvasId,width:t.canvasWidth,height:t.canvasHeight},on:{mousedown:function(e){return t.onMouseDown(e)},mousemove:function(e){return t.onMouseMove(e)},mouseup:function(e){return t.onMouseUp()},click:function(e){return t.onClick(e)},dblclick:function(e){return t.onDoubleClick(e)}}})])},i=[],o=a("2909"),r=(a("ac6a"),a("fa7d")),s={name:"RoiDrawPanel",components:{},data:function(){return{canvasId:r["a"].randomString(),roiImageId:r["a"].randomString(),roiImgClass:"roiImgClassNormal",roiCanvasClass:"roiCanvasClassNormal",canvasWidth:1,canvasHeight:1,roiPaths:[],drawingPath:[],mouseIsDown:!1,mouseCurrX:0,mouseCurrY:0}},props:{imgSrc:{type:String,required:!1,default:""},panelShown:{type:Boolean,required:!1,default:!1},isDrawing:{type:Boolean,required:!1,default:!1},modelValue:{required:!0}},model:{prop:"modelValue",event:"input"},computed:{},methods:{canvasBoxToImageBox:function(){},imageBoxToCanvasBox:function(){},imageLoaded:function(){var t=this,e=document.getElementById(this.roiImageId);!this.panelShown||e.naturalWidth?(this.canvasWidth=e.width,this.canvasHeight=e.height,this.loadRoiPaths(this.modelValue),setTimeout((function(){t.drawRois()}),200)):setTimeout((function(){return t.imageLoaded()}),300)},drawPath:function(t,e,a){0!==e.length&&(t.save(),a?(t.strokeStyle="rgba(30, 200, 30, 1)",t.fillStyle="rgba(30, 200, 30, 1)",t.fillRect(e[0][0]-1,e[0][1]-1,3,3)):t.strokeStyle="rgba(30, 30, 200, 1)",t.beginPath(),t.lineWidth=2,t.moveTo(e[0][0],e[0][1]),e.slice(1).forEach((function(e){return t.lineTo(e[0],e[1])})),t.closePath(),t.stroke(),t.restore())},drawRois:function(){var t=this,e=document.getElementById(this.canvasId),a=document.createElement("canvas");a.width=e.width,a.height=e.height;var n,i=a.getContext("2d");this.roiPaths.forEach((function(e){t.drawPath(i,e,!1)})),n=this.mouseIsDown?[].concat(Object(o["a"])(this.drawingPath),[[this.mouseCurrX,this.mouseCurrY]]):this.drawingPath,n.length&&this.drawPath(i,n,!0);var r=i.getImageData(0,0,a.width,a.height),s=e.getContext("2d");s.putImageData(r,0,0)},filterRoiPaths:function(){},roiPathsToEvent:function(){if(!this.roiPaths.length)return null;var t=document.getElementById(this.roiImageId),e=t.naturalWidth/this.canvasWidth,a=t.naturalHeight/this.canvasHeight,n=this.roiPaths.map((function(t){return t.map((function(t){return[Math.round(t[0]*e),Math.round(t[1]*a)]}))}));return console.log("roiPathsToEvent",n),JSON.stringify(n)},resetRois:function(){this.roiPaths=[],this.drawingPath=[]},loadRoiPaths:function(t){if(t){var e=document.getElementById(this.roiImageId);try{var a=this.canvasWidth/e.naturalWidth,n=this.canvasHeight/e.naturalHeight,i=JSON.parse(t);this.roiPaths=i.map((function(t){return t.map((function(t){return[Math.round(t[0]*a),Math.round(t[1]*n)]}))}))}catch(o){console.log("loadRoiPaths exception",o)}console.log("loadRoiPaths",this.roiPaths)}else this.resetRois()},onMouseDown:function(t){console.log("onMouseDown",t),this.isDrawing&&1===t.buttons&&(this.mouseIsDown=!0,this.mouseCurrX=t.offsetX,this.mouseCurrY=t.offsetY,this.drawRois())},onMouseMove:function(t){this.isDrawing&&1===t.buttons&&this.mouseIsDown&&this.drawingPath.length&&(this.mouseCurrX=t.offsetX,this.mouseCurrY=t.offsetY,this.drawRois())},onMouseUp:function(t){console.log("onMouseUp",t),this.isDrawing&&this.mouseIsDown&&(this.mouseIsDown=!1,this.drawingPath.push([this.mouseCurrX,this.mouseCurrY]))},onClick:function(t){console.log("onClick",t)},onDoubleClick:function(t){console.log("onDoubleClick",t)}},watch:{isDrawing:function(){!this.isDrawing&&this.drawingPath.length>=3&&(this.roiPaths.push(this.drawingPath),this.$emit("input",this.roiPathsToEvent())),this.drawingPath=[],this.drawRois()},panelShown:function(){var t=this;this.panelShown&&setTimeout((function(){return t.imageLoaded()}),500)},modelValue:function(){console.log("roi modelValue changed",this.modelValue),this.loadRoiPaths(this.modelValue),this.drawRois()}},mounted:function(){}},u=s,c=(a("fc8b"),a("2877")),l=Object(c["a"])(u,n,i,!1,null,null,null);e["a"]=l.exports},"4f58":function(t,e,a){},"61d5":function(t,e,a){},"6c7b":function(t,e,a){var n=a("5ca1");n(n.P,"Array",{fill:a("36bd")}),a("9c6c")("fill")},"83a1":function(t,e){t.exports=Object.is||function(t,e){return t===e?0!==t||1/t===1/e:t!=t&&e!=e}},f62b:function(t,e,a){"use strict";a("6c7b");var n=function(){var t=this,e=t._self._c;return e("div",{staticClass:"w-100 h-100 overflow-auto"},[e("div",{staticClass:"row",staticStyle:{height:"10px"}}),e("div",{staticClass:"row mx-0"},[e("div",[e("label",{staticClass:"ml-2 mr-2 pl-2",attrs:{for:t.uniqueId+"weekday-same"}},[t._v("每天监控时段相同")]),e("input",{directives:[{name:"model",rawName:"v-model",value:t.weekdaySame,expression:"weekdaySame"}],attrs:{type:"checkbox",id:t.uniqueId+"weekday-same"},domProps:{checked:Array.isArray(t.weekdaySame)?t._i(t.weekdaySame,null)>-1:t.weekdaySame},on:{change:function(e){var a=t.weekdaySame,n=e.target,i=!!n.checked;if(Array.isArray(a)){var o=null,r=t._i(a,o);n.checked?r<0&&(t.weekdaySame=a.concat([o])):r>-1&&(t.weekdaySame=a.slice(0,r).concat(a.slice(r+1)))}else t.weekdaySame=i}}})])]),t._l(t.weekdays,(function(a,n){return e("div",{key:t.uniqueId+"-weekday-"+n,staticClass:"row mx-0 my-0"},[e("div",{staticClass:"pl-2 py-2 text-center",staticStyle:{width:"16%"}},[e("label",{staticClass:"mr-2",attrs:{for:t.uniqueId+"weekday-selected"+n}},[t._v("星期"+t._s(a))]),e("input",{directives:[{name:"model",rawName:"v-model",value:t.dayStatus[n],expression:"dayStatus[i]"}],attrs:{type:"checkbox",id:t.uniqueId+"weekday-selected"+n},domProps:{checked:Array.isArray(t.dayStatus[n])?t._i(t.dayStatus[n],null)>-1:t.dayStatus[n]},on:{change:function(e){var a=t.dayStatus[n],i=e.target,o=!!i.checked;if(Array.isArray(a)){var r=null,s=t._i(a,r);i.checked?s<0&&t.$set(t.dayStatus,n,a.concat([r])):s>-1&&t.$set(t.dayStatus,n,a.slice(0,s).concat(a.slice(s+1)))}else t.$set(t.dayStatus,n,o)}}})]),e("div",{},[e("div",{staticClass:"d-flex"},t._l(new Array(25).fill(0).map((function(t,e){return e})),(function(a,i){return e("div",{key:t.uniqueId+"-time-label-"+n+"-"+i,staticClass:"time-label-sm"},[t._v("\n          "+t._s(a)+"\n        ")])})),0),e("div",{staticClass:"time-tick-sm ml-1 mr-0"}),e("div",{staticClass:"time-bar-sm ml-1 mr-0"},t._l(new Array(t.dayCellNum).fill(0).map((function(t,e){return e})),(function(a,i){return e("div",{key:t.uniqueId+"-time-cell-"+n+"-"+i,class:"time-cell-sm"+(t.cellStatus[n*t.dayCellNum+i]?" cell-selected":"")+(t.dayStatus[n]?"":" day-disabled"),on:{mousedown:function(e){return e.stopPropagation(),t.onTimeCellDown(e,n,i)},mouseover:function(e){return e.stopPropagation(),t.onTimeCellOver(e,n,i)},mouseout:function(e){return e.stopPropagation(),t.onTimeCellOut(e,n,i)},mouseup:function(e){return e.stopPropagation(),t.onTimeCellUp(e,n,i)}}})})),0)]),e("div",{staticClass:"pl-2 py-2 text-center",staticStyle:{width:"4%"}},[e("a",{staticClass:"popover-dismiss",attrs:{type:"button",role:"button","data-toggle":"popover",title:"","data-content":t.getDayTimeDesc(n),"data-original-title":"已设置时间段"}},[e("IconFont",{attrs:{iconName:"icon-xiangxixinxi"}})],1)])])}))],2)},i=[],o=a("2909"),r=(a("ac6a"),a("fa7d")),s=a("1157"),u=a.n(s),c=7,l=30,d=1440/l,h=c*d;function m(){for(var t=new Array(h).fill(0),e=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,40,41,42,43,44,45,46,47],a=function(a){e.forEach((function(e){t[a*d+e]=1}))},n=0;n<c;n++)a(n);return t}var f={name:"WeekDatetimePicker",components:{},data:function(){return{uniqueId:r["a"].randomId("uniqueId"),currDay:-1,weekdayNum:c,dayCellNum:d,timeCellSize:l,dayStatus:new Array(c).fill(!0),cellStatus:m(),weekdaySame:!1,weekdays:["一","二","三","四","五","六","日"]}},props:{modelValue:{type:String}},model:{prop:"modelValue",event:"input"},computed:{},methods:{formatTimeValue:function(t){return t<10?"0".concat(t):"".concat(t)},getDayTimeSegs:function(t){var e=[],a=0;while(a<this.dayCellNum){while(a<this.dayCellNum&&!this.cellStatus[t*this.dayCellNum+a])a+=1;if(a<this.dayCellNum){var n=a;while(a<this.dayCellNum&&this.cellStatus[t*this.dayCellNum+a])a+=1;var i=a;e.push([n*this.timeCellSize,i*this.timeCellSize])}}return e},segsToCellStatus:function(t){var e=this,a=new Array(h).fill(0);t.forEach((function(t,n){t.segs.forEach((function(t){for(var i=Math.floor(t[0]/l),o=Math.ceil(t[1]/l),r=i;r<o;r++)a[n*e.dayCellNum+r]=1}))})),this.cellStatus=a},getDayTimeDesc:function(t){var e=this,a="",n=this.getDayTimeSegs(t);return a=n.map((function(t){return"".concat(e.formatTimeValue(Math.floor(t[0]/60)),":").concat(e.formatTimeValue(t[0]%60),"-").concat(e.formatTimeValue(Math.floor(t[1]/60)),":").concat(e.formatTimeValue(t[1]%60))})).join(";"),a},getDateTimeSettings:function(){for(var t=[],e=0;e<this.weekdayNum;e++)t.push({enabled:this.dayStatus[e],segs:this.getDayTimeSegs(e)});return t},setDateTimeSettings:function(t){var e=this;t&&t.length===this.weekdayNum&&(t.forEach((function(t,a){e.dayStatus[a]^t.enabled&&(e.dayStatus[a]=t.enabled)})),this.segsToCellStatus(t))},makeWeekdaySame:function(t){for(var e=0;e<this.weekdayNum;e++)if(e!==t)for(var a=0;a<this.dayCellNum;a++)this.cellStatus[e*this.dayCellNum+a]=this.cellStatus[t*this.dayCellNum+a]},onTimeCellDown:function(t,e,a){1===t.buttons&&this.dayStatus[e]&&(this.currDay=e,this.cellStatus[e*this.dayCellNum+a]^=1,this.cellStatus=Object(o["a"])(this.cellStatus),this.weekdaySame&&this.makeWeekdaySame(this.currDay))},onTimeCellOver:function(t,e,a){1===t.buttons&&(this.currDay<0||e!==this.currDay||(this.cellStatus[e*this.dayCellNum+a]^=1,this.cellStatus=Object(o["a"])(this.cellStatus),this.weekdaySame&&this.makeWeekdaySame(this.currDay)))},onTimeCellOut:function(t,e){1===t.buttons&&(this.currDay<0||this.currDay)},onTimeCellUp:function(t,e,a){1===t.buttons&&(this.currDay=-1)}},watch:{weekdaySame:function(){this.weekdaySame&&this.makeWeekdaySame(0),this.$emit("input",JSON.stringify(this.getDateTimeSettings()))},dayStatus:{handler:function(){this.$emit("input",JSON.stringify(this.getDateTimeSettings()))},deep:!0},cellStatus:function(){this.$emit("input",JSON.stringify(this.getDateTimeSettings()))},modelValue:{handler:function(t){t?this.setDateTimeSettings(JSON.parse(t)):(this.dayStatus=new Array(c).fill(!0),this.cellStatus=m())},deep:!0}},mounted:function(){u()((function(){u()('[data-toggle="popover"]').popover()}))}},g=f,y=(a("1938"),a("2877")),v=Object(y["a"])(g,n,i,!1,null,null,null);e["a"]=v.exports},fa7d:function(t,e,a){"use strict";a("456d"),a("ac6a");var n=a("53ca");a("7514"),a("28a5"),a("a481"),a("3b2b"),a("386d");e["a"]={nextTableSelectedIndex:function(t,e){var a=e+1;while(a<t.length){if(t[a].selected)break;a++}return a},downloadFile:function(t){var e=document.createElement("iframe");e.style.display="none",e.style.height=0,e.src=t,document.body.appendChild(e),setTimeout((function(){e.remove()}),3e5)},randomString:function(t){for(var e=t||8,a="ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678",n=a.length,i="",o=0;o<e;o++)i+=a.charAt(Math.floor(Math.random()*n));return i},randomId:function(t){return"".concat(t,"-").concat(this.randomString())},getProtocolHostPort:function(){var t=document.location.protocol;":"===!t.substr(t.length-1,1)&&(t+=":");var e=document.location.host;return e.search(":"+document.location.port)<0&&(e+=":"+document.location.port),"".concat(t,"//").concat(e)},getThumbPathPrefix:function(){return"".concat(this.getProtocolHostPort(),"/nc19api/v1/fileservice/images/")},getThumbPathPostfix:function(t){return"thumb/?thumb_size=".concat(t,"&id=")},replaceChinese:function(t){var e={"：":":","，":",","；":";","？":"?","‘":"'","’":"'","“":'"',"”":'"',"！":"!","＃":"#","＆":"&","×":"*","（":"(","）":")","－":"-","—":"_","＋":"+","＝":"=","｛":"{","｝":"}","【":"[","】":"]","｜":"|","～":"~","《":"<","》":">","​":"","＞":">","＜":"<","★":"*","。":". ","、":"\\","∽":"~","￠":"","":"","氧传感":"Oxygen Sensor","(盎司)":"(ounces)","．":". "};for(var a in e){var n=new RegExp(a,"g");t=t.replace(n,e[a])}return t},filterEnglishOrSymbol:function(t){return t&&t.search(/[\u4e00-\u9fa5]/)>=0?"Chinese Characters":""},getProductEditUrl:function(t,e,a,n,i){var o=t.$router.resolve({path:"/products/products/productedit",query:{product_id:e,source:a,auto_save:n?1:0,view_only:i?1:0}});return o},openProductEditPageEx:function(t,e,a,n){var i=this.getProductEditUrl(t,e,a,n);window.open(i.href,"_blank")},openProductEditPage:function(t,e,a){this.openProductEditPageEx(t,e,a,0)},getDateFromDateTimeString:function(t){return t.split("T")[0]},getImageThumbById:function(t,e,a){var n="".concat(t.img_root,"thumb/?id=").concat(e);return a&&(n="".concat(n,"&thumb_size=").concat(a)),n},getImageThumbByName:function(t,e,a){var n="".concat(t.img_root,"thumb/").concat(e);return a&&(n="".concat(n,"?thumb_size=").concat(a)),n},getImageLinkByName:function(t,e){return"".concat(t.img_root).concat(e)},getLabelFromOptionMap:function(t,e,a,n){var i=t.find((function(t){return t[e]===n}));return i[a]},getDayDiff:function(t,e){return(new Date(t).getTime()-new Date(e))/864e5},defaultApiErrorHandler:function(t,e){return function(a){console.log("".concat(t," failed(").concat(e,"): "),a),"response"in a&&"data"in a.response&&a.response.data instanceof Object&&"data"in a.response.data&&a.response.data.data}},arrayEqual:function(t,e){if(!t||!e)return!t&&!e;if(t.length!==e.length)return!1;for(var a=0;a<t.length;a++)if(t[a]instanceof Array&&e[a]instanceof Array){if(!this.arrayEqual(t[a],e[a]))return!1}else if(t[a]!==e[a])return!1;return!0},deepCopy:function(t){var e=this;if(null===t||"object"!==Object(n["a"])(t))return t;var a=Array.isArray(t)?[]:{};return Object.keys(t).forEach((function(n){a[n]=e.deepCopy(t[n])})),a},eval:function(t){var e=Function;return new e("return "+t)()},getImageUrl:function(t){return"".concat("/static/images","/").concat(t)}}},fc8b:function(t,e,a){"use strict";a("61d5")}}]);