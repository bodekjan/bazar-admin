$(function(){
      'use strict';
      $(".remove").click(function () {
          var meId = $(this).attr("id");
          var d = dialog({
              title: 'Message',
              content: 'wakaaaaaaaaaaaaaaaaaaaaa',
              okValue: 'yes',
              ok: function () {
                  location.href = "employeelist.html?method=delete&id=" + meId;
                  return false;
              },
              cancelValue: 'cancel',
              cancel: function () { }
          });
          d.show();
      });
      $(".editemp").click(function () {
          var meId = $(this).attr("id");
          setCookie("parentpage", window.location.search.substr(1));
          location.href = "/addemployee?method=edit&id=" + meId;
      });
      $("#addemp").click(function () {
          setCookie("parentpage", window.location.search.substr(1));
          location.href = "/addemployee";
      });
});
