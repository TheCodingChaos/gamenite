

import React from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';

function SignupForm({ onSignup }) {
  const formik = useFormik({
    initialValues: {
      name: '',
      email: '',
      password: ''
    },
    validationSchema: Yup.object({
      name: Yup.string().required('Required'),
      email: Yup.string().email('Invalid email address').required('Required'),
      password: Yup.string().min(6, 'Must be at least 6 characters').required('Required')
    }),
    onSubmit: (values, { setSubmitting, setErrors }) => {
      fetch('/signup', {
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
          onSignup(data);
        })
        .catch(err => {
          setErrors({ email: err.error || 'Signup failed' });
        })
        .finally(() => setSubmitting(false));
    }
  });

  return (
    <form onSubmit={formik.handleSubmit}>
      <h2>Sign Up</h2>
      <div>
        <label>Name</label>
        <input
          name="name"
          onChange={formik.handleChange}
          value={formik.values.name}
        />
        {formik.errors.name && <div>{formik.errors.name}</div>}
      </div>
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
      <button type="submit" disabled={formik.isSubmitting}>Sign Up</button>
    </form>
  );
}

export default SignupForm;