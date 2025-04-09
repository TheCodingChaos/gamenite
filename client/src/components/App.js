import React, { useState } from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import routes from "../routes";

function App() {
  const [user, setUser] = useState(null);

  return (
    <Routes>
      {routes.map(({ path, element, protected: isProtected }) => (
        <Route
          key={path}
          path={path}
          element={
            isProtected && !user ? (
              <Navigate to="/login" replace />
            ) : React.cloneElement(element, {
                onLogin: setUser,
                onSignup: setUser,
                user
            })
          }
        />
      ))}
    </Routes>
  );
}

export default App;
