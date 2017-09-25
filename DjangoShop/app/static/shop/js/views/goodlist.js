$(function(){
      'use strict';
      $(".remove").click(function () {
          var meId = $(this).attr("id");
          var d = dialog({
              title: 'Message',
              content: 'wakaaaaaaaaaaaaaaaaaaaaa',
              okValue: 'yes',
              ok: function () {
                  location.href = "goodlist.html?method=delete&id=" + meId;
                  return false;
              },
              cancelValue: 'cancel',
              cancel: function () { }
          });
          d.show();
      });
      $(".editgood").click(function () {
          var meId = $(this).attr("id");
          setCookie("parentpage", window.location.search.substr(1));
          location.href = "/addgood?method=edit&id=" + meId;
      });
      $("#search").click(function () {
          location.href = "/goodlist?key=" + $("#stext").val() + "&type=" + $("#type-selector").find("option:selected").val();
      });
      $("#type-selector").change(function () {
          location.href = "/goodlist?key=" + $("#stext").val() + "&type=" + $("#type-selector").find("option:selected").val();
      });
      function GetQueryString(name) {
          var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
          var r = window.location.search.substr(1).match(reg);
          if (r != null) return unescape(r[2]); return null;
      }
      $("#addgood").click(function () {
          setCookie("parentpage", window.location.search.substr(1));
          location.href = "/addgood";
      });
      
});
