

import React from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';

function LoginForm({ onLogin }) {
  const formik = useFormik({
    initialValues: {
      email: '',
      password: ''
    },
    validationSchema: Yup.object({
      email: Yup.string().email('Invalid email address').required('Required'),
      password: Yup.string().required('Required')
    }),
    onSubmit: (values, { setSubmitting, setErrors }) => {
      fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(values)
      })
        .then(res => {
          if (res.ok) return res.json();
          return res.json().then(err => Promise.reject(err));
        })
        .then(data => {
          onLogin(data);
        })
        .catch(err => {
          setErrors({ email: err.error || 'Login failed' });
        })
        .finally(() => setSubmitting(false));
    }
  });

  return (
    <form onSubmit={formik.handleSubmit}>
      <h2>Login</h2>
      <div>
        <label>Email</label>
        <input
          type="email"
          name="email"
          onChange={formik.handleChange}
          value={formik.values.email}
        />
        {formik.errors.email && <div>{formik.errors.email}</div>}
      </div>
      <div>
        <label>Password</label>
        <input
          type="password"
          name="password"
          onChange={formik.handleChange}
          value={formik.values.password}
        />
        {formik.errors.password && <div>{formik.errors.password}</div>}
      </div>
      <button type="submit" disabled={formik.isSubmitting}>Login</button>
    </form>
  );
}

export default LoginForm;