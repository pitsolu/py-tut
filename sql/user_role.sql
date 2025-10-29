SELECT u.id as user_id, u.email as user_email, u.password as user_password,
		r.id as role_id, r.name as role_name, r.descr as role_descr
FROM user u
LEFT JOIN role r ON u.role_id = r.id
WHERE u.email = ?