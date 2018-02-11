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
      var toast = new Toast('success', 'toast-bottom-left', pid + ' added to collection!');
      showToast(toast);
      target.parents(".card").find(".view").removeClass("hm-black-strong");
      target.fadeOut(300, function() {
      target.remove();
      });
    },
    error: function(reponse) {
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
  modal.find('#modalConfirmDeleteButton').attr('data-product-id', product_id);
});

$("#modalConfirmDeleteButton").click(function(event) {
  var pid = event.target.dataset.productId;
  $.ajax({
    url: "/delete",
    type: "get",
    data: {
      product_id: pid
    },
    success: function(response) {
      var toast = new Toast('success', 'toast-bottom-left', pid + ' deleted from collection!');
      showToast(toast);
      $("#" + pid).fadeOut(600, function() {
        $("#" + pid).remove();
      });
    },
    error: function(response) {
      var toast = new Toast('error', 'toast-bottom-left', pid + ' cannot be deleted from collection!');
      showToast(toast);
    }
  });
  $("#modalConfirmDelete").modal('hide');
  return false;
});

