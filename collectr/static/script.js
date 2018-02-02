function Toast(type, css, msg) {
  this.type = type;
  this.css = css;
  this.msg = msg;
}


function showToast(t) {
  toastr.options.positionClass = t.css;
  toastr[t.type](t.msg);
}


$(".alert-target").click(function () {
  var target = $(this);
  var pid = target.data("product-id");
  $.ajax({
    url: "/add",
    type: "get",
    data: {
      product_id: pid
    }, 
    success: function(response) {
      console.log("ok");
      var toast = new Toast('success', 'toast-bottom-left', pid + ' added to collection!');
      showToast(toast);
      target.parents(".card").find(".view").removeClass("hm-black-strong");
      target.fadeOut(300, function() {
        target.remove();
      });
    },
    error: function(reponse) {
      console.log("error");
      var toast = new Toast('error', 'toast-bottom-left', pid + ' cannot be added to collection!');
      showToast(toast);
    }
  });
  return false;
});


$("#modalConfirmDelete").on('show.bs.modal', function (event) {
  var action = $(event.relatedTarget);
  var product_id = action.data('product-id');
  var modal = $(this);
  modal.find('.modal-body #product-id').text(product_id);
});

