import Vue from "vue";
import Router from "vue-router";

import ListOfProjects from "./mycomponents/ListOfProjects/ListOfProjects.vue";
import Project from "./mycomponents/Project/Project.vue";
import Run from "./mycomponents/Run/Run.vue";
import TestDataViewer from "./mycomponents/TestDataViewer/TestDataViewer.vue";
import TestDataViewer1 from "./mycomponents/TestDataViewer1/TestDataViewer1.vue";
import Login from "./mycomponents/Login/Login.vue";
// import AddProject from "./views/AddProject.vue";
import store from './store/index.js';

Vue.use(Router);

const router= new Router({
  routes: [
    {
      path: "/",
      name: "Projects",
      component: ListOfProjects,
      meta: { requiresAuth: true }
    },
    {
      path: "/project/:project_id",
      component: Project, 		
      props: true,
      meta: { requiresAuth: true }
    },
    { 
      path: '/run/:run_id', 		
      component: Run,		 		
      props: true ,
      meta: { requiresAuth: true }
    },
    { 
      path: '/ViewTestData/:project_id', 		
      component: TestDataViewer,
      props: true ,
      meta: { requiresAuth: true }
    },
    { 
      path: '/ViewTestData1/:project_id', 		
      component: TestDataViewer1,
      props: true ,
      meta: { requiresAuth: true },
      name: 'TestDataViewer1'
    },
    {
      path: "/Login",
      component: Login,
      meta: { requiresUnauth: true } 
    },
    // { 
    //   path: '/addproject/:user_id', 
    //   component: AddProject, 	
    //   props: true
    // },    
    { 
      path: '*', 
      redirect: '/' 
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/About.vue")
    }
  ]
});

router.beforeEach(function(to, _, next) {
  if (to.meta.requiresAuth && !store.getters.isAuthenticated) {
    console.log("isAuthenticated ",  store.getters.isAuthenticated )
    console.log("forwarding to login");
    next('/login');
  } else if (to.meta.requiresUnauth && store.getters.isAuthenticated) {
    next('');
  } else {
    next();
  }
});

export default router;
