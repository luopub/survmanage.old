(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-3bb5c302"],{3214:function(t,e,a){"use strict";a("6c34")},4447:function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t._self._c;return e("div",{staticClass:"container-fluid"},[e("div",{staticClass:"row w-100 ml-1 my-2"},[e("div",{staticClass:"row ml-1 my-2"},[e("button",{staticClass:"btn btn-primary",attrs:{"data-toggle":"modal","data-target":"#"+t.channelEditDlgId}},[t._v("添加通道")]),e("button",{staticClass:"btn btn-light ml-4",attrs:{disabled:!0}},[t._v("已用通道 "+t._s(t.usedNos.length)+"/"+t._s(t.availNos.length))])]),e("div",{staticClass:"row w-100"},[e("ApiDataTable",{attrs:{handlers:t.tableHandlers,tableId:"channelListTableId",dataHeight:400,showWaitingDlg:!1,showSearch:!1,detailView:!1}})],1),e("ChannelEditDlg",{attrs:{modalId:t.channelEditDlgId,channelId:t.currRowChannelId,availNos:t.availNos},on:{"channel-saved":t.onChannelSaved}}),e("ChannelDeleteDlg",{attrs:{modalId:t.channelDeleteDlgId,channelId:t.currRowChannelId,cno:t.currRowChannelNo},on:{"channel-deleted":t.onChannelDeleted}}),e("ChannelAlgConfigDlg",{attrs:{modalId:t.channelAlgConfigDlgId,channelId:t.currRowChannelId,cno:t.currRowChannelNo,channelName:t.currRowChannelName},on:{"channel-deleted":t.onChannelAlgSaved}})],1)])},o=[],i=(a("ac6a"),a("7f7f"),a("55dd"),a("2909")),l=a("f217"),s=a("fa7d"),r=a("1157"),c=a.n(r),d=function(){var t=this,e=t._self._c;return e("SimpleModalDlg",{attrs:{modalId:t.modalId,title:t.channelId?"编辑通道":"添加通道",content:"",defaultButtonText:"取消",button2Text:"保存",button2Action:t.button2Action,dialogWidth:600},scopedSlots:t._u([{key:"bodyPost",fn:function(){return[e("div",{staticClass:"container-fluid"},[e("div",{staticClass:"row"},[e("div",{staticClass:"col-3"},[e("span",{staticClass:"field-label field-required"},[t._v("通道号")])]),e("div",{staticClass:"col mb-1"},[e("select",{directives:[{name:"model",rawName:"v-model",value:t.cno,expression:"cno"}],attrs:{name:"selectList"},on:{change:function(e){var a=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.cno=e.target.multiple?a:a[0]}}},t._l(t.availNos,(function(a){return e("option",{key:t.modalId+a},[t._v(t._s(a))])})),0),e("IconFont",{class:t.cnoValid?"dagou-icon":"dacha-icon",attrs:{iconName:t.cnoValid?"icon-dagouyouquan":"icon-cuowuguanbiquxiao-yuankuang"}})],1)]),e("div",{staticClass:"row"},[e("div",{staticClass:"col-3"},[e("span",{staticClass:"field-label field-required"},[t._v("通道ID")])]),e("div",{staticClass:"col mb-1"},[e("input",{directives:[{name:"model",rawName:"v-model",value:t.cid,expression:"cid"}],staticClass:"mr-1",staticStyle:{width:"20em"},domProps:{value:t.cid},on:{input:function(e){e.target.composing||(t.cid=e.target.value)}}}),e("IconFont",{class:t.cidValid?"dagou-icon":"dacha-icon",attrs:{iconName:t.cidValid?"icon-dagouyouquan":"icon-cuowuguanbiquxiao-yuankuang"}})],1)]),e("div",{staticClass:"row"},[e("div",{staticClass:"col-3"},[e("span",{staticClass:"field-label field-required"},[t._v("通道名称")])]),e("div",{staticClass:"col mb-1"},[e("input",{directives:[{name:"model",rawName:"v-model",value:t.name,expression:"name"}],staticClass:"mr-1",staticStyle:{width:"20em"},domProps:{value:t.name},on:{input:function(e){e.target.composing||(t.name=e.target.value)}}}),e("IconFont",{class:t.nameValid?"dagou-icon":"dacha-icon",attrs:{iconName:t.nameValid?"icon-dagouyouquan":"icon-cuowuguanbiquxiao-yuankuang"}})],1)]),e("div",{staticClass:"row"},[e("div",{staticClass:"col-3"},[e("span",{staticClass:"field-label field-required"},[t._v("通道位置")])]),e("div",{staticClass:"col mb-1"},[e("input",{directives:[{name:"model",rawName:"v-model",value:t.site,expression:"site"}],staticClass:"mr-1",staticStyle:{width:"20em"},domProps:{value:t.site},on:{input:function(e){e.target.composing||(t.site=e.target.value)}}}),e("IconFont",{class:t.siteValid?"dagou-icon":"dacha-icon",attrs:{iconName:t.siteValid?"icon-dagouyouquan":"icon-cuowuguanbiquxiao-yuankuang"}})],1)]),e("div",{staticClass:"row"},[e("div",{staticClass:"col-3"},[e("span",{staticClass:"field-label field-required"},[t._v("URL")])]),e("div",{staticClass:"col mb-1"},[e("input",{directives:[{name:"model",rawName:"v-model",value:t.url,expression:"url"}],staticClass:"mr-1",staticStyle:{width:"20em"},domProps:{value:t.url},on:{input:function(e){e.target.composing||(t.url=e.target.value)}}}),e("IconFont",{class:t.urlValid?"dagou-icon":"dacha-icon",attrs:{iconName:t.urlValid?"icon-dagouyouquan":"icon-cuowuguanbiquxiao-yuankuang"}})],1)])])]},proxy:!0}])})},u=[],h=(a("c5f6"),a("f953")),m=a("0be2"),f={name:"ChannelEditDlg",components:{SimpleModalDlg:h["a"]},data:function(){return{cno:"",cid:"",name:"",site:"",url:""}},props:{modalId:{type:String,required:!0},channelId:{type:Number,required:!0},availNos:{type:Array,required:!0}},computed:{cnoValid:function(){return!!this.cno},cidValid:function(){return 32===this.cid.trim().length},nameValid:function(){return this.name.trim().length>0},siteValid:function(){return this.site.length>0},urlValid:function(){return this.url.length>=10}},methods:{button2Action:function(){var t=this,e="channel/channels/",a={};if(this.cnoValid)if(a["cno"]=this.cno,this.cidValid)if(a["cid"]=this.cid.trim(),this.nameValid)if(a["name"]=this.name.trim(),this.siteValid)if(a["site"]=this.site.trim(),this.urlValid){a["url"]=this.url.trim();var n=m["a"].apiAjaxPost;this.channelId&&(e="".concat(e).concat(this.channelId,"/"),n=m["a"].apiAjaxPut),n(e,a,(function(e){0===e.code?(alert("通道信息保存成功！"),t.$emit("channel-saved")):alert("通道信息保存失败(".concat(e.code,"): ").concat(e.message))}),s["a"].defaultApiErrorHandler(e,""))}else alert("通道URL不能为空！");else alert("通道位置不能为空！");else alert("通道名称不能为空！");else alert("通道ID为32位16进制数字！");else alert("请选择正确的通道号")},clearFields:function(){this.cno="",this.cid="",this.name="",this.site="",this.url=""},loadChannel:function(){var t=this,e="channel/channels/".concat(this.channelId,"/");m["a"].apiAjaxGet(e,{},(function(e){0===e.code?(t.cno=e.data.cno,t.cid=e.data.cid,t.name=e.data.name,t.site=e.data.site,t.url=e.data.url):alert("通道信息加载失败(".concat(e.code,"): ").concat(e.message))}),s["a"].defaultApiErrorHandler(e,""))}},watch:{channelId:function(t){t?this.loadChannel():this.clearFields()}},mounted:function(){}},g=f,p=a("2877"),b=Object(p["a"])(g,d,u,!1,null,null,null),v=b.exports,w=function(){var t=this,e=t._self._c;return e("SimpleModalDlg",{attrs:{modalId:t.modalId,title:"删除通道",content:"所有该通道产生的报警信息都会被删除。确认删除通道（".concat(t.cno,"）吗？"),defaultButtonText:"取消",button2Text:"确认",button2Action:t.button2Action,dialogWidth:500}})},C=[],y={name:"ChannelDeleteDlg",components:{SimpleModalDlg:h["a"]},data:function(){return{}},props:{modalId:{type:String,required:!0},channelId:{type:Number,required:!0},cno:{type:Number,required:!0}},computed:{},methods:{button2Action:function(){var t=this,e="channel/channels/".concat(this.channelId,"/"),a={};m["a"].apiAjaxDelete(e,a,(function(){alert("通道删除成功！"),t.$emit("channel-deleted")}),s["a"].defaultApiErrorHandler(e,""))}},watch:{},mounted:function(){}},S=y,I=Object(p["a"])(S,w,C,!1,null,null,null),_=I.exports,x=(a("456d"),function(){var t=this,e=t._self._c;return e("SimpleModalDlg",{attrs:{modalId:t.modalId,title:"算法配置 - 通道 ".concat(t.cno," - ").concat(t.channelName),content:"",defaultButtonText:"取消",button2Text:"确定",button2Action:t.saveStatus,dialogWidth:1100},scopedSlots:t._u([{key:"bodyPost",fn:function(){return[e("div",{staticClass:"container-fluid"},[e("div",{staticClass:"row"},[e("div",{staticClass:"col-3"},[e("div",{staticClass:"w-100 overflow-auto border-top border-bottom",staticStyle:{height:"620px"}},[e("div",{staticClass:"list-group",attrs:{id:"list-tab",role:"tablist"}},t._l(Object.keys(t.channelAlgInfo),(function(a,n){return e("a",{key:"alg"+t.modalId+n,class:"list-group-item list-group-item-action "+(0===n?"active":""),attrs:{id:"".concat(t.modalId,"-list-").concat(a),"data-toggle":"list","data-x":a,role:"tab"}},[e("div",{staticClass:"icon-name"},[e("div",{staticClass:"mr-2",staticStyle:{"max-height":"100%",width:"60px"}},[e("img",{attrs:{src:t.channelAlgInfo[a].icon,alt:""}})]),e("div",{staticStyle:{width:"90px"}},[e("p",{staticClass:"mb-1"},[e("b",[t._v(t._s(t.channelAlgInfo[a].name_ch)+"识别")])]),e("p",{staticClass:"my-0"},[e("IconFont",{class:t.channelAlgInfo[a].channelAlgorthm?"dagou-icon":"dacha-icon",attrs:{iconName:t.channelAlgInfo[a].channelAlgorthm?"icon-dagouyouquan":"icon-cuowuguanbiquxiao-yuankuang"}}),t._v("\n                      "+t._s(t.channelAlgInfo[a].channelAlgorthm?"已配置":"未配置")+"\n                    ")],1)])])])})),0)])]),e("div",{staticClass:"col-9 pl-0"},[e("div",{staticClass:"w-100 overflow-auto border-top border-bottom container-fluid",staticStyle:{height:"620px"}},[e("ChannelAlgConfigPanel",{attrs:{algDisplayName:t.channelAlgInfo[t.currAlgName].name_ch,channelImage:t.channelImage,modalShown:t.modalShown,defaultParameters:t.defaultParameters},model:{value:t.algStatus[t.currAlgName],callback:function(e){t.$set(t.algStatus,t.currAlgName,e)},expression:"algStatus[currAlgName]"}})],1)])])])]},proxy:!0}])})}),D=[],O=(a("8e6e"),a("ade3")),P=a("8715"),A=a("b84e");function N(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,n)}return a}function T(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?N(Object(a),!0).forEach((function(e){Object(O["a"])(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):N(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}var j={name:"ChannelAlgConfigDlg",components:{SimpleModalDlg:h["a"],ChannelAlgConfigPanel:A["a"]},data:function(){return{channelAlgInfo:P["a"].getAlgNameIcons(),currAlgName:Object.keys(P["a"].getAlgoritims())[0],algStatus:P["a"].initDefaultAlgStatus(),dateTimeSettingShown:!1,channelImage:"",modalShown:!1,defaultParameters:{}}},props:{modalId:{type:String,required:!0},channelId:{type:Number,required:!0},cno:{type:Number,required:!0},channelName:{type:String,required:!0}},computed:{},methods:{saveStatus:function(){var t=this,e="channel/channels/".concat(this.channelId,"/config_alg/"),a=this.algStatus;m["a"].apiAjaxPost(e,a,(function(e){0===e.code?(alert("通道（".concat(t.cno,"）算法配置保存成功！")),t.$emit("channel-alg-saved")):alert("通道（".concat(t.cno,"）算法配置保存失败(").concat(e.code,"): ").concat(e.message)),t.loadChannelAlgorithms()}),s["a"].defaultApiErrorHandler(e,""))},loadChannelAlgorithms:function(){var t=this,e="channel/channelalgorithms2/?channel=".concat(this.channelId);m["a"].apiAjaxGet(e,{},(function(e){if(0===e.code){for(var a in t.channelAlgInfo)t.channelAlgInfo[a].channelAlgorthm=null;Object.keys(t.channelAlgInfo).forEach((function(e){var a=T({configured:!1},t.defaultParameters);t.algStatus[e]=a})),e.data.forEach((function(e){e.algorithm.name in Object.keys(t.channelAlgInfo)?alert("发现不认识的算法: ".concat(e.algorithm.name)):(t.channelAlgInfo[e.algorithm.name].channelAlgorthm=e,t.algStatus[e.algorithm.name]=t.recordToStatus(e))})),console.log("loadChannelAlgorithms2",t.algStatus)}else console.log("获取通道算法失败！")}),s["a"].defaultApiErrorHandler(e,""))},recordToStatus:function(t){var e={};return Object.keys(this.defaultParameters).forEach((function(a){e[a]=t[a]})),e.configured=!0,e},loadChannelImage:function(){var t=this;if(this.channelId){var e="channel/channels/".concat(this.channelId,"/get_real_time_image/");m["a"].apiAjaxGet(e,{},(function(e){0===e.code&&e.data&&(t.channelImage=s["a"].getImageUrl(e.data.filename))}),s["a"].defaultApiErrorHandler(e,""))}},loadDefaultParameters:function(){var t=this,e="algorithm/algorithmdefaultparameters/";m["a"].apiAjaxGet(e,{},(function(e){if(0===e.code)if(e.data.length>0)for(var a in t.defaultParameters={},P["a"].defaultAlgParams)t.defaultParameters[a]=e.data[0][a];else t.defaultParameters=T({},P["a"].defaultAlgParams)}),s["a"].defaultApiErrorHandler(e,""))}},watch:{channelId:function(){this.loadChannelAlgorithms(),this.loadChannelImage()},currAlgName:function(){},algStatus:{handler:function(){},deep:!0}},mounted:function(){var t=this;c()('a[data-toggle="list"]').on("shown.bs.tab",(function(e){t.currAlgName=c()(e.target).attr("data-x")})),c()("#dateTimeSetting").on("hidden.bs.collapse",(function(){t.dateTimeSettingShown=!1})),c()("#dateTimeSetting").on("shown.bs.collapse",(function(){t.dateTimeSettingShown=!0})),c()("#".concat(this.modalId)).on("shown.bs.modal",(function(){t.modalShown=!0})),c()("#".concat(this.modalId)).on("hide.bs.modal",(function(){t.modalShown=!1})),this.loadDefaultParameters()}},q=j,k=(a("89ea"),Object(p["a"])(q,x,D,!1,null,null,null)),R=k.exports;window.channelRowSelected=function(t,e,a){window.currRowChannelId=t,window.currRowChannelNo=e,window.currRowChannelName=a};var F={name:"ModuleChConfig",components:{ApiDataTable:l["a"],ChannelEditDlg:v,ChannelDeleteDlg:_,ChannelAlgConfigDlg:R},data:function(){return{channelListTableId:s["a"].randomId("tableId"),channelEditDlgId:s["a"].randomId("modalId"),channelDeleteDlgId:s["a"].randomId("modalId"),channelAlgConfigDlgId:s["a"].randomId("modalId"),tableComp:null,currRowChannelId:0,currRowChannelNo:0,currRowChannelName:"",freeNos:[1,2,3,4,5,6,7,8],usedNos:[]}},computed:{tableHandlers:function(){return{setComponent:this.tableSetComponent,getEndpoint:this.tableGetEndPoint,getParams:this.tableGetParams,tableRowFormatter:this.tableRowFormatter,getColSpecs:this.tableGetColSpecs,rowStyle:this.rowStyle,getDataList:this.getDataList,onPageLoaded:this.onPageLoaded}},availNos:function(){var t=[].concat(Object(i["a"])(this.freeNos),Object(i["a"])(this.usedNos));return t.sort()}},methods:{onChannelSaved:function(){this.reloadTable(),this.getUsedFreeChannels()},onChannelDeleted:function(){this.reloadTable(),this.getUsedFreeChannels()},onChannelAlgSaved:function(){},tableSetComponent:function(t){this.tableComp=t},tableRowFormatter:function(t){return{id:t.id,cno:t.cno,cid:t.cid,name:t.name,site:t.site,url:t.url,status:"...",operation:'\n          <div style="display:inline;">\n            <a class="icon-anchor" href="javascript:channelRowSelected('.concat(t.id,", ").concat(t.cno,", '").concat(t.name,"');$('#").concat(this.channelEditDlgId,'\').modal(\'show\')">\n              <div class="icon-box-green">\n                <i class="icon iconfont icon-bianji icon-inbox-white"></i>\n              </div>\n            </a>\n            <a class="icon-anchor" href="javascript:channelRowSelected(').concat(t.id,", ").concat(t.cno,", '").concat(t.name,"');$('#").concat(this.channelDeleteDlgId,'\').modal(\'show\')">\n              <div class="icon-box-red">\n                <i class="icon iconfont icon-shanchu icon-inbox-white"></i>\n              </div>\n            </a>\n          </div>\n        ')}},tableGetParams:function(){return{ordering:"cno"}},tableGetEndPoint:function(){return"channel/channels/"},tableGetColSpecs:function(){var t=[{field:"id",title:"ID",visible:!1},{field:"cno",title:"通道编号"},{field:"cid",title:"通道ID"},{field:"name",title:"通道名称"},{field:"site",title:"通道位置"},{field:"url",title:"URL"},{field:"status",title:"状态"},{field:"operation",title:"操作"}];return t},onTableSelectionChanged:function(){},reloadTable:function(){this.tableComp&&this.tableComp.getOnePage(),this.onTableSelectionChanged()},onPageLoaded:function(t,e){var a=this,n="channel/channels/get_real_time_status/?channel_ids=".concat(e.map((function(t){return t.id})).join(","));console.log("onPageLoaded",e,n),m["a"].apiAjaxGet(n,{},(function(t){0===t.code&&e.forEach((function(e,n){e.id in t.data&&a.tableComp.table.bootstrapTable("updateCell",{index:n,field:"status",value:'\n                  <span class="icon iconfont icon-dot" style="color: '.concat(t.data[e.id]?"green":"gray",';"></span>\n                  ').concat(t.data[e.id]?"在线":"离线","\n                ")})}))}),s["a"].defaultApiErrorHandler(n,""))},rowStyle:function(){var t={};return t},getDataList:function(t){return t.data.results},getUsedFreeChannels:function(){var t=this,e="channel/channels/get_used_free_channel_nos/";m["a"].apiAjaxGet(e,{},(function(e){0===e.code&&(t.freeNos=e.data.free_nos,t.usedNos=e.data.used_nos)}),s["a"].defaultApiErrorHandler(e,""))},beforeModalShow:function(){this.currRowChannelId=window.currRowChannelId,this.currRowChannelNo=window.currRowChannelNo,this.currRowChannelName=window.currRowChannelName,console.log("beforeModalShow",this.currRowChannelId,this.currRowChannelNo,this.currRowChannelName)}},mounted:function(){var t=this;c()("#".concat(this.channelEditDlgId)).on("show.bs.modal",(function(e){"relatedTarget"in e?t.currRowChannelId=0:t.beforeModalShow()})),c()("#".concat(this.channelDeleteDlgId)).on("show.bs.modal",(function(){t.beforeModalShow()})),c()("#".concat(this.channelAlgConfigDlgId)).on("show.bs.modal",(function(){t.beforeModalShow()})),this.getUsedFreeChannels()}},E=F,V=Object(p["a"])(E,n,o,!1,null,null,null);e["default"]=V.exports},"6c34":function(t,e,a){},8236:function(t,e,a){},"89ea":function(t,e,a){"use strict";a("8236")},b84e:function(t,e,a){"use strict";var n=function(){var t=this,e=t._self._c;return e("div",{staticClass:"container-fluid"},[t.showTitle?e("div",{staticClass:"row w-100 ml-1 py-2 border-bottom"},[e("label",{staticClass:"mt-1 field-label"},[t._v("当前算法：")]),e("span",{staticClass:"mt-1 mr-4"},[t._v(t._s(t.algDisplayName)+"识别")]),e("label",{staticClass:"mt-1 field-label",attrs:{for:"id-channel-alg-config"}},[t._v("配置")]),e("input",{directives:[{name:"model",rawName:"v-model",value:t.status.configured,expression:"status.configured"}],staticClass:"ml-1",attrs:{type:"radio",id:"id-channel-alg-config",name:"channelAlgConfig"},domProps:{value:!0,checked:t._q(t.status.configured,!0)},on:{change:function(e){return t.$set(t.status,"configured",!0)}}}),e("label",{staticClass:"ml-2 mt-1 field-label",attrs:{for:"id-channel-alg-unconfig"}},[t._v("不配置")]),e("input",{directives:[{name:"model",rawName:"v-model",value:t.status.configured,expression:"status.configured"}],staticClass:"ml-2",attrs:{type:"radio",id:"id-channel-alg-unconfig",name:"channelAlgConfig"},domProps:{value:!1,checked:t._q(t.status.configured,!1)},on:{change:function(e){return t.$set(t.status,"configured",!1)}}}),e("button",{staticClass:"btn btn-sm btn-primary ml-2",attrs:{type:"button"},on:{click:t.restoreDefault}},[t._v("恢复默认参数")])]):t._e(),e("div",{directives:[{name:"show",rawName:"v-show",value:t.status.configured,expression:"status.configured"}],staticClass:"row mt-2 pb-2 border-bottom"},[e("span",{staticClass:"field-label pl-3"},[t._v("检测参数：")]),e("div",{staticClass:"container-fluid"},[e("div",{staticClass:"row"},[t._m(0),e("div",{staticClass:"col"},[e("input",{directives:[{name:"model",rawName:"v-model.number",value:t.status.analyze_interval,expression:"status.analyze_interval",modifiers:{number:!0}}],staticClass:"ml-2",attrs:{type:"number",step:"500"},domProps:{value:t.status.analyze_interval},on:{input:function(e){e.target.composing||t.$set(t.status,"analyze_interval",t._n(e.target.value))},blur:function(e){return t.$forceUpdate()}}}),e("span",{},[t._v("(500毫秒为单位，最小值1000毫秒)")])])]),e("div",{staticClass:"row mt-1"},[t._m(1),e("div",{staticClass:"col"},[e("input",{directives:[{name:"model",rawName:"v-model.number",value:t.status.alert_interval,expression:"status.alert_interval",modifiers:{number:!0}}],staticClass:"ml-2",attrs:{type:"number",step:"1"},domProps:{value:t.status.alert_interval},on:{input:function(e){e.target.composing||t.$set(t.status,"alert_interval",t._n(e.target.value))},blur:function(e){return t.$forceUpdate()}}})])]),e("div",{staticClass:"row mt-1"},[t._m(2),e("div",{staticClass:"col"},[e("input",{directives:[{name:"model",rawName:"v-model.number",value:t.status.alert_threshold,expression:"status.alert_threshold",modifiers:{number:!0}}],staticClass:"ml-2",attrs:{type:"number",step:"0.05"},domProps:{value:t.status.alert_threshold},on:{input:function(e){e.target.composing||t.$set(t.status,"alert_threshold",t._n(e.target.value))},blur:function(e){return t.$forceUpdate()}}}),e("span",{},[t._v("(值越大检查准确率越高)")])])])])]),e("div",{directives:[{name:"show",rawName:"v-show",value:t.status.configured,expression:"status.configured"}],staticClass:"row mt-2 pb-2 border-bottom"},[e("div",{staticClass:"container-fluid"},[e("div",{staticClass:"row mb-1"},[e("span",{staticClass:"field-label pl-3 pt-1"},[t._v("布控时间：")]),e("a",{directives:[{name:"show",rawName:"v-show",value:t.showTimeToggle,expression:"showTimeToggle"}],staticClass:"btn-sm btn-primary",attrs:{"data-toggle":"collapse",href:"#dateTimeSetting",role:"button","aria-expanded":"false","aria-controls":"dateTimeSetting"}},[t._v(t._s(t.dateTimeSettingShown?"收起":"展开"))])]),e("div",{staticClass:"row"},[e("div",{class:"col collapse ".concat(t.showTimeToggle?"":"show"),attrs:{id:"dateTimeSetting"}},[e("div",{staticClass:"border w-100",staticStyle:{height:"400px"}},[e("WeekDatetimePicker",{model:{value:t.status.alert_times,callback:function(e){t.$set(t.status,"alert_times",e)},expression:"status.alert_times"}})],1)])])])]),e("div",{directives:[{name:"show",rawName:"v-show",value:t.status.configured&&t.showRoi,expression:"status.configured && showRoi"}],staticClass:"row mt-2 border-bottom"},[e("div",{staticClass:"container-fluid"},[e("div",{staticClass:"row"},[e("span",{staticClass:"field-label py-2 pl-3"},[t._v("绘制监控区域(ROI)：")]),e("a",{staticClass:"mr-2",attrs:{title:t.roiDrawing?"完成":"新建多边形",href:"javascript:void(0);"},on:{click:function(e){t.roiDrawing=!t.roiDrawing}}},[e("IconFont",{class:t.roiDrawing?"duobianxing-selected":"duobianxing-unselected",attrs:{iconName:"icon-duobianxingxuanze"}})],1),e("a",{staticClass:"mr-2",attrs:{title:"清除选区(监控整个画面)",href:"javascript:void(0);"},on:{click:function(e){t.status.roi_region=null,t.roiDrawing=!1}}},[e("IconFont",{staticClass:"shanchu-button",attrs:{iconName:"icon-shanchu"}})],1)]),e("div",{staticClass:"row mt-2"},[e("div",{staticClass:"col"},[e("RoiDrawPanel",{attrs:{isDrawing:t.roiDrawing,imgSrc:t.channelImage,panelShown:t.modalShown&&t.status.configured},model:{value:t.status.roi_region,callback:function(e){t.$set(t.status,"roi_region",e)},expression:"status.roi_region"}})],1)])])])])},o=[function(){var t=this,e=t._self._c;return e("div",{staticClass:"col-3 text-right"},[e("span",{},[t._v("分析间隔(毫秒)")])])},function(){var t=this,e=t._self._c;return e("div",{staticClass:"col-3 text-right"},[e("span",{},[t._v("报警间隔(秒)")])])},function(){var t=this,e=t._self._c;return e("div",{staticClass:"col-3 text-right"},[e("span",{},[t._v("报警阈值(0-1)")])])}],i=(a("8e6e"),a("ac6a"),a("456d"),a("ade3")),l=a("f62b"),s=a("4865"),r=a("d940");function c(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,n)}return a}function d(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?c(Object(a),!0).forEach((function(e){Object(i["a"])(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):c(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}var u={name:"ChannelAlgConfigPanel",components:{WeekDatetimePicker:l["a"],RoiDrawPanel:s["a"],IconFont:r["a"]},data:function(){return{dateTimeSettingShown:!1,status:{},algDisplayNamePrev:"",roiDrawing:!1}},props:{defaultParameters:{type:Object,required:!1,default:function(){return{}}},showTimeToggle:{type:Boolean,required:!1,default:!0},showTitle:{type:Boolean,required:!1,default:!0},showRoi:{type:Boolean,required:!1,default:!0},channelImage:{type:String,required:!1,default:""},modalShown:{type:Boolean,required:!1,default:!1},algDisplayName:{type:String,required:!0},modelValue:{type:Object,required:!0}},model:{prop:"modelValue",event:"input"},computed:{},methods:{restoreDefault:function(){var t=d({},this.status);for(var e in this.defaultParameters)t[e]=this.defaultParameters[e];this.status=t}},watch:{modelValue:function(t){this.algDisplayNamePrev===this.algDisplayName&&JSON.stringify(this.status)===JSON.stringify(t)||(this.algDisplayNamePrev=this.algDisplayName,this.status=this.modelValue)},status:{handler:function(){console.log("this.status changed",this.status),this.$emit("input",this.status)},deep:!0},algDisplayName:function(){this.roiDrawing=!1}},mounted:function(){this.status=d({},this.modelValue)}},h=u,m=(a("3214"),a("2877")),f=Object(m["a"])(h,n,o,!1,null,null,null);e["a"]=f.exports},f217:function(t,e,a){"use strict";var n=function(){var t=this,e=t._self._c;return e("div",{staticClass:"container-fluid w-100 overflow-auto"},[e("table",{staticClass:"text-nowrap",attrs:{id:t.tableId,"data-height":t.dataHeight,"data-classes":"table table-striped table-sm","data-sortable":"true","data-click-to-select":"true","data-pagination":t.pagination,"data-side-pagination":"server","data-detail-view":t.detailView,"data-detail-view-icon":"true","data-detail-view-by-click":"true","data-show-footer":t.showFooter}})])},o=[],i=(a("8e6e"),a("456d"),a("2909")),l=(a("ac6a"),a("7514"),a("ade3")),s=(a("c5f6"),{transCellSelected2ItemSelected:function(t,e,a,n){var o=0,i=null;n&&(o=n.id,i=n),"selectedId"in t&&(t.selectedId=o),"selectedRow"in t&&(t.selectedRow=i),t.$emit("itemSelected",o,i)}}),r=a("1157"),c=a.n(r),d=a("0be2");function u(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,n)}return a}function h(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?u(Object(a),!0).forEach((function(e){Object(l["a"])(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):u(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}var m={name:"ApiDataTable",components:{},data:function(){return{table:null,listSize:10,listOffset:0,searchText:"",sortOrder:"",sortField:"",timeoutIdReload:0,selectedIds:[],selectedRows:[]}},props:{tableId:{type:String,required:!1,default:"api_data_table"},handlers:{type:Object,required:!0},dataHeight:{type:Number,required:!1,default:500},loadData:{type:Boolean,required:!1,default:!0},inModal:{type:Boolean,required:!1,default:!1},showSearch:{type:Boolean,required:!1,default:!0},showFooter:{type:Boolean,required:!1,default:!1},detailView:{type:Boolean,required:!1,default:!0},pagination:{type:Boolean,required:!1,default:!0},checkbox:{type:Boolean,required:!1,default:!1}},methods:{detailFormatter:function(t,e){return"undefined"===typeof this.handlers.detailFormatter?this.defaultDetailFormatter(t,e):this.handlers.detailFormatter(t,e)},rowStyle:function(t,e){return"undefined"===typeof this.handlers.rowStyle?{}:this.handlers.rowStyle(t,e)},defaultDetailFormatter:function(t,e){var a=[];a.push('<div class="text-left"><pre>');var n=JSON.stringify(e,null,4);return a.push(n),a.push("</pre></div>"),a.join("")},getOnePage:function(){var t=this,e=this.handlers.getEndpoint();if(e){var a={limit:this.listSize,offset:this.listOffset,search:this.searchText,order:this.sortOrder,order_field:this.sortField};if(Object.assign(a,this.getSortParam()),"getParams"in this.handlers&&this.handlers.getParams){var n=this.handlers.getParams();n&&(a=h(h({},a),n))}d["a"].apiAjaxGet(e,a,(function(e){if(0===e.code){var a=e.data,n=t.handlers.getDataList?t.handlers.getDataList(e):a.rows,o=[];for(var i in n){var l=t.handlers.tableRowFormatter(n[i],i,t);o.push(l)}t.table.bootstrapTable("load",o),t.table.bootstrapTable("refreshOptions",{totalRows:a.count}),t.handlers.onPageLoaded&&t.handlers.onPageLoaded(t,o)}else console.log("Got getOnePage error: "),console.log(e.data)}),(function(t){console.log(t)}),(function(){t.onTableSelectionChanged(),t.onTableDblClickCell(null,null,null,null)}))}},onSearch:function(t,e){this.searchText=e,console.log("onSearch",e)},onPageChange:function(t,e,a){console.log("onPageChange: ",e,a),this.listSize=a,this.listOffset=(e-1)*this.listSize,this.searchText=this.table.bootstrapTable("getOptions").searchText,this.getOnePage()},getSortParam:function(){var t=this.table.bootstrapTable("getOptions"),e=t.sortName,a=t.sortOrder;if(t.sortName)e=t.sortName,a=t.sortOrder;else{var n=t.columns[0].find((function(t){return"default-sort-order"in t}));if(!n)return{};e=n.field,a=n["default-sort-order"]}var o=e,i=t.columns[0].find((function(t){return t.field===e}));return"sort-name"in i&&(o=i["sort-name"]),o={asc:"",desc:"-"}[a]+o,console.log("onSort: ".concat(e,", ").concat(a,", ").concat(o),t),{ordering:o}},onTableDblClickCell:function(t,e,a,n){this.$emit("cellSelected",e,a,n)},getRowIndex:function(t,e){var a=-1,n=this.table.bootstrapTable("getData");return n.forEach((function(n,o){n[t]===e&&(a=o)})),a},refreshSelectedRow:function(t,e,a){var n=this.getRowIndex(t,e);n>=0&&this.table.bootstrapTable("showRow",{index:n});var o=this.getRowIndex(t,a);o>=0&&this.table.bootstrapTable("showRow",{index:o})},delayToReleadTable:function(t){var e=this;this.timeoutIdReload&&(clearTimeout(this.timeoutIdReload),this.timeoutIdReload=0),t&&(this.listOffset=0),this.timeoutIdReload=setTimeout((function(){e.timeoutIdReload=0,e.getOnePage()}),500)},onTableSelectionChanged:function(){this.selectedRows=this.table.bootstrapTable("getSelections"),this.selectedIds=this.selectedRows.map((function(t){return t.id})),this.$emit("selection-changed",this.selectedIds,this.selectedRows)},setEventForCheckbox:function(){this.checkbox&&(this.table.on("check.bs.table",this.onTableSelectionChanged),this.table.on("uncheck.bs.table",this.onTableSelectionChanged),this.table.on("check-all.bs.table",this.onTableSelectionChanged),this.table.on("uncheck-all.bs.table",this.onTableSelectionChanged))}},computed:{},watch:{loadData:function(t){t&&this.getOnePage()},checkbox:function(){this.setEventForCheckbox()}},mounted:function(){this.handlers.setComponent(this);var t=this.handlers.getColSpecs();this.checkbox&&(t=[{field:"selected",checkbox:!0,default:!1}].concat(Object(i["a"])(t)));var e=c()("#".concat(this.tableId));this.table=e,e.bootstrapTable({columns:t,pageNumber:1,pageSize:this.listSize,pageList:"[10, 20, 50, 100]",paginationHAlign:"right",paginationDetailHAlign:"left",detailFormatter:this.detailFormatter,rowStyle:this.rowStyle,search:this.showSearch,showJumpTo:!0}),e.on("search.bs.table",this.onSearch),e.on("sort.bs.table",this.getOnePage),e.on("page-change.bs.table",this.onPageChange),e.on("dbl-click-cell.bs.table",this.onTableDblClickCell),this.setEventForCheckbox(),this.loadData&&this.getOnePage()},transCellSelected2ItemSelected:function(t,e,a,n){s.transCellSelected2ItemSelected(t,e,a,n)}},f=m,g=a("2877"),p=Object(g["a"])(f,n,o,!1,null,"33d5ac98",null);e["a"]=p.exports},f953:function(t,e,a){"use strict";var n=function(){var t=this,e=t._self._c;return e("ModalDlgFrame",{attrs:{modalId:t.modalId,dialogWidth:t.dialogWidth,titleBg:t.titleBg,showClose:t.showClose},scopedSlots:t._u([{key:"title",fn:function(){return[t._v("\n    "+t._s(t.title)+"\n  ")]},proxy:!0},{key:"body",fn:function(){return[t._t("bodyPre"),t.content.length>0?e("pre",{staticClass:"text-left"},[t._v(t._s(t.content))]):t._e(),t._t("bodyPost")]},proxy:!0},{key:"footer",fn:function(){return[t._t("footerPre"),e("button",{directives:[{name:"show",rawName:"v-show",value:!!t.defaultButtonText,expression:"!!defaultButtonText"}],staticClass:"btn btn-default btn-primary",attrs:{type:"button","data-dismiss":"modal"},on:{click:t.defaultButtonAction}},[t._v("\n      "+t._s(t.defaultButtonText)+"\n    ")]),t.button2Text?e("button",{staticClass:"btn btn-outline-primary",attrs:{type:"button","data-dismiss":"modal"},on:{click:t.button2Action}},[t._v("\n      "+t._s(t.button2Text)+"\n    ")]):t._e(),t.button3Text?e("button",{staticClass:"btn btn-outline-primary",attrs:{type:"button","data-dismiss":"modal"},on:{click:t.button3Action}},[t._v("\n      "+t._s(t.button3Text)+"\n    ")]):t._e(),t._t("footerPost")]},proxy:!0}],null,!0)})},o=[],i=(a("c5f6"),function(){var t=this,e=t._self._c;return e("div",{staticClass:"container-fluid"},[e("div",{staticClass:"modal fade modal-open",attrs:{"data-backdrop":"static",id:t.modalId,tabindex:"-1",role:"dialog"}},[e("div",{staticClass:"modal-dialog draggable align-self-center",attrs:{role:"document"}},[e("div",{staticClass:"modal-content",style:t.contentStyle},[e("div",{class:"modal-header panel-heading py-0 "+t.titleBg,staticStyle:{border:"0px"}},[e("h5",{staticClass:"modal-title"},[t._t("title")],2),t.showClose?e("button",{staticClass:"close",attrs:{type:"button","data-dismiss":"modal","aria-label":"Close"}},[e("span",{attrs:{"aria-hidden":"true"}},[t._v("×")])]):t._e()]),e("div",{staticClass:"modal-body"},[t._t("body")],2),e("div",{staticClass:"modal-footer",staticStyle:{border:"0px"}},[t._t("footer")],2)])])])])}),l=[],s=a("1157"),r=a.n(s),c={name:"ModalDlgFrame",props:{modalId:{type:String,required:!0},titleBg:{type:String,required:!1,default:"bg-primary"},dialogWidth:{type:Number,required:!1,default:800},showClose:{type:Boolean,required:!1,default:!0}},data:function(){return{}},methods:{modalCenter:function(){var t=r()("#".concat(this.modalId," ")+".modal-dialog");if(t.is(":visible")){r()("#".concat(this.modalId)).css("display","block");var e=r()("#".concat(this.modalId," ")+".modal-content"),a=e.outerHeight(!0),n=e.outerWidth(!0),o=r()(window).height()/2-a/2;o<10&&(o=10),t.css("margin-top",o+"px");var i=r()(window).width()/2-n/2;t.css("margin-left",i+"px")}}},computed:{contentStyle:function(){return{width:this.dialogWidth+"px"}}},created:function(){},mounted:function(){r()("#".concat(this.modalId)).on("shown.bs.modal",this.modalCenter),r()(window).on("resize",this.modalCenter)}},d=c,u=a("2877"),h=Object(u["a"])(d,i,l,!1,null,"3348ccfd",null),m=h.exports,f={name:"SimpleModalDlg",components:{ModalDlgFrame:m},data:function(){return{}},props:{modalId:{type:String,required:!0},titleBg:{type:String,required:!1,default:""},defaultButtonText:{type:String,required:!1,default:"Close"},defaultButtonAction:{type:Function,required:!1,default:function(){}},button2Text:{type:String,required:!1,default:""},button2Action:{type:Function,required:!1,default:function(){}},button3Text:{type:String,required:!1,default:""},button3Action:{type:Function,required:!1,default:function(){}},title:{type:String,required:!1,default:"Simple Dialog"},content:{type:String,required:!1,default:""},dialogWidth:{type:Number,required:!1,default:600},showClose:{type:Boolean,required:!1,default:!0}},mounted:function(){}},g=f,p=Object(u["a"])(g,n,o,!1,null,null,null);e["a"]=p.exports}}]);