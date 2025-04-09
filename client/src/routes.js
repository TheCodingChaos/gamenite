

import React from "react";
import LoginForm from "./pages/LoginForm";
import SignupForm from "./pages/SignupForm";

const routes = [
  {
    path: "/login",
    element: <LoginForm />
  },
  {
    path: "/signup",
    element: <SignupForm />
  },
  {
    path: "/",
    element: <h1>Home Page</h1>,
    protected: true
  }
];

export default routes;