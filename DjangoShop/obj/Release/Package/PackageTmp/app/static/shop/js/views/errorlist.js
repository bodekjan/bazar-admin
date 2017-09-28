$(function(){
      'use strict';
      $("#mysql").click(function () {
          var d = dialog({
              title: '<p>??????????</p>',
              content: '???????? ??????? ?????????? ?????????? ?? ????? ????? ????????? ?????????? ??????? ?????? ????? ??? ?????? ?????????',
              okValue: 'yes',
              ok: function () {
                  var csrftoken = getCookie('csrftoken');
                  $.ajaxSetup({
                      beforeSend: function (xhr, settings) {
                          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                              xhr.setRequestHeader("X-CSRFToken", csrftoken);
                          }
                      }
                  });
                  $.post("/sys",
                      {
                          command: "mysql"
                      },
                      function (data, status) {
                          alert("Data: " + data.msg + "\nStatus: " + status);
                          if (data.status == "success") {
                              $(".sysbtn").hide();
                              $("#sysmsg").html(data.msg);
                          }
                      }
                  );
                  d.close().remove();
                  return false;
              },
              cancelValue: 'cancel',
              cancel: function () { }
          });
          d.show();
      });
      $("#apache").click(function () {
          var d = dialog({
              title: '<p>??????????</p>',
              content: '???????? ??????? ?????????? ?????????? ?? ????? ????? ????????? ?????????? ??????? ?????? ????? ??? ?????? ?????????',
              okValue: 'yes',
              ok: function () {
                  var csrftoken = getCookie('csrftoken');
                  $.ajaxSetup({
                      beforeSend: function (xhr, settings) {
                          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                              xhr.setRequestHeader("X-CSRFToken", csrftoken);
                          }
                      }
                  });
                  $.post("/sys",
                      {
                          command: "apache"
                      },
                      function (data, status) {
                          $(".sysbtn").hide();
                          $("#sysmsg").html(data.msg);
                      }
                  );
                  d.close().remove();
                  return false;
              },
              cancelValue: 'cancel',
              cancel: function () { }
          });
          d.show();
      });
      $("#win").click(function () {
          var d = dialog({
              title: '<p>??????????</p>',
              content: '???????? ??????? ?????????? ?????????? ?? ????? ????? ????????? ?????????? ??????? ?????? ????? ??? ?????? ?????????',
              okValue: 'yes',
              ok: function () {
                  var csrftoken = getCookie('csrftoken');
                  $.ajaxSetup({
                      beforeSend: function (xhr, settings) {
                          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                              xhr.setRequestHeader("X-CSRFToken", csrftoken);
                          }
                      }
                  });
                  $.post("/sys",
                      {
                          command: "win"
                      },
                      function (data, status) {
                          $(".sysbtn").hide();
                          $("#sysmsg").html(data.msg);
                      }
                  );
                  d.close().remove();
                  return false;
              },
              cancelValue: 'cancel',
              cancel: function () { }
          });
          d.show();
      });
});
