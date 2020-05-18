var calendar1 = function(l) {
  "use strict";
  var e = function() {
    (this.$body = l("body")),
      (this.$modal = l("#event-modal")),
      (this.$event = "#external-events div.external-event"),
      (this.$calendar = l("#calendar")),
      (this.$saveCategoryBtn = l(".save-category")),
      (this.$categoryForm = l("#add-category form")),
      (this.$extEvents = l("#external-events")),
      (this.$calendarObj = null);
  };
  (e.prototype.onDrop = function(e, t) {
    var n = e.data("eventObject"),
      a = e.attr("data-class"),
      o = l.extend({}, n);
    (o.start = t),
      a && (o.className = [a]),
      this.$calendar.fullCalendar("renderEvent", o, !0),
      l("#drop-remove").is(":checked") && e.remove();
  }),
    (e.prototype.onEventClick = function(t, e, n) {
      console.log("onEventClick")
      var a = this,
        o = l("<form></form>");
      o.append("<label>Change event name</label>"),
        o.append(
          "<div class='input-group m-b-15'><input class='form-control' type=text value='" +
            t.title +
            "' /><span class='input-group-append'><button type='submit' class='btn btn-success btn-md waves-effect waves-light'><i class='fa fa-check'></i> Save</button></span></div>"
        ),
        a.$modal.modal({ backdrop: "static" }),
        a.$modal
          .find(".delete-event")
          .show()
          .end()
          .find(".save-event")
          .hide()
          .end()
          .find(".modal-body")
          .empty()
          .prepend(o)
          .end()
          .find(".delete-event")
          .unbind("click")
          .click(function() {
            a.$calendarObj.fullCalendar("removeEvents", function(e) {
              return e._id == t._id;
            }),
              a.$modal.modal("hide");
          }),
        a.$modal.find("form").on("submit", function() {
          return (
            (t.title = o.find("input[type=text]").val()),
            a.$calendarObj.fullCalendar("updateEvent", t),
            a.$modal.modal("hide"),
            !1
          );
        });
    }),
    (e.prototype.onSelect = function(n, a, e) {
      console.log("onSelect")
      // console.log(n, a, e)
      var o = this;
      console.log(this.$modal.modal)
      o.$modal.modal({ backdrop: "static" });
      var i = l("<form></form>");
      i.append("<div class='row'></div>"),
        i
          .find(".row")
          .append(
            "<div class='col-md-6'><div class='form-group'><label class='control-label'>Event Name</label><input class='form-control' placeholder='Insert Event Name' type='text' name='title'/></div></div>"
          )
          .append(
            "<div class='col-md-6'><div class='form-group'><label class='control-label'>Category</label><select class='form-control' name='category'></select></div></div>"
          )
          .find("select[name='category']")
          .append("<option value='bg-danger'>Danger</option>")
          .append("<option value='bg-success'>Success</option>")
          .append("<option value='bg-purple'>Purple</option>")
          .append("<option value='bg-primary'>Primary</option>")
          .append("<option value='bg-pink'>Pink</option>")
          .append("<option value='bg-info'>Info</option>")
          .append("<option value='bg-inverse'>Inverse</option>")
          .append("<option value='bg-warning'>Warning</option></div></div>"),
        o.$modal
          .find(".delete-event")
          .hide()
          .end()
          .find(".save-event")
          .show()
          .end()
          .find(".modal-body")
          .empty()
          .prepend(i)
          .end()
          .find(".save-event")
          .unbind("click")
          .click(function() {
            i.submit();
          }),
        o.$modal.find("form").on("submit", function() {
          var e = i.find("input[name='title']").val(),
            t =
              (i.find("input[name='beginning']").val(),
              i.find("input[name='ending']").val(),
              i.find("select[name='category'] option:checked").val());
          return (
            null !== e && 0 != e.length
              ? (o.$calendarObj.fullCalendar(
                  "renderEvent",
                  { title: e, start: n, end: a, allDay: !1, className: t },
                  !0
                ),
                o.$modal.modal("hide"))
              : alert("You have to give a title to your event"),
            !1
          );
        }),
        o.$calendarObj.fullCalendar("unselect");
    }),
    (e.prototype.enableDrag = function() {
      l(this.$event).each(function() {
        var e = { title: l.trim(l(this).text()) };
        l(this).data("eventObject", e),
          l(this).draggable({ zIndex: 999, revert: !0, revertDuration: 0 });
      });
    }),
    (e.prototype.init = function() {
      this.enableDrag();
      var e = new Date(),
        t = (e.getDate(), e.getMonth(), e.getFullYear(), new Date(l.now())),
        n = [
          {
            title: "Hey!",
            start: new Date(l.now() + 158e6),
            className: "bg-purple",
          },
          { title: "See John Deo", start: t, end: t, className: "bg-success" },
          {
            title: "Meet John Deo",
            start: new Date(l.now() + 168e6),
            className: "bg-info",
          },
          {
            title: "Buy a Theme",
            start: new Date(l.now() + 338e6),
            className: "bg-primary",
          },
        ],
        a = this;
      (a.$calendarObj = a.$calendar.fullCalendar({
        slotDuration: "00:15:00",
        minTime: "08:00:00",
        maxTime: "19:00:00",
        defaultView: "agendaWeek",
        handleWindowResize: !0,
        height: l(window).height() - 200,
        header: {
          left: "prev,next today",
          center: "title",
          right: "month,agendaWeek,agendaDay",
        },
        events: n,
        editable: !0,
        droppable: !0,
        eventLimit: !0,
        selectable: !0,
        drop: function(e) {
          a.onDrop(l(this), e);
        },
        select: function(e, t, n) {
          a.onSelect(e, t, n);
        },
        eventClick: function(e, t, n) {
          a.onEventClick(e, t, n);
        },
      })),
        this.$saveCategoryBtn.on("click", function() {
          var e = a.$categoryForm.find("input[name='category-name']").val(),
            t = a.$categoryForm.find("select[name='category-color']").val();
          null !== e &&
            0 != e.length &&
            (a.$extEvents.append(
              '<div class="external-event bg-' +
                t +
                '" data-class="bg-' +
                t +
                '" style="position: relative;"><i class="mdi mdi-checkbox-blank-circle mr-2 vertical-middle"></i>' +
                e +
                "</div>"
            ),
            a.enableDrag());
        });
    }),
    (l.CalendarApp = new e()),
    (l.CalendarApp.Constructor = e);
};

var calendar2 = function(e) {
    "use strict";
    window.jQuery.CalendarApp.init();
};

export{
    calendar1,calendar2
}
