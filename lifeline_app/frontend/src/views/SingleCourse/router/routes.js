import mainpage from "../../../components/mainpage";
import homework from "../../../components/homework";
import notice from "../../../components/notice";
import document from "../../../components/document";

export default [
  {
    path: "/",
    name: "home",
    component: () => lazyLoadView(import("../../../components/home")),
    meta: {
      authRequired: true,
      title: "Dashboard"
    },
    children: [
      { path: "mainpage", name: "mainpage", component: mainpage },
      { path: "homework", name: "homework", component: homework },
      { path: "notice", name: "notice", component: notice },
      { path: "document", name: "document", component: document }
    ]
  }
];

function lazyLoadView(AsyncView) {
  const AsyncHandler = () => ({
    component: AsyncView,
    // A component to use while the component is loading.
    loading: require("../../../components/_loading").default,
    // Delay before showing the loading component.
    // Default: 200 (milliseconds).
    delay: 400,
    // A fallback component in case the timeout is exceeded
    // when loading the component.
    error: require("../../../components/_timeout").default,
    // Time before giving up trying to load the component.
    // Default: Infinity (milliseconds).
    timeout: 10000
  });

  return Promise.resolve({
    functional: true,
    render(h, { data, children }) {
      // Transparently pass any props or children
      // to the view component.
      return h(AsyncHandler, data, children);
    }
  });
}
