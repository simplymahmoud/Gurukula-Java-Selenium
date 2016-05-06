package testsuite;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.util.ArrayList;
import java.util.List;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;


import framework.factory;
import framework.model.BranchPage;

public class Branch extends factory{
	
	List<String> Branches = new ArrayList<String>();

	@Before
	public void test_setup() throws Exception {
		click_login();
		fill_login("admin", "admin");
		click_authenticat();
		click_entities_branch_menu();
	}
	
	@After
	public void test_teardown() throws Exception {
		for(String branch: Branches){
			delete_branch(branch);
		}
	}	
	
	@Test
	public void Branch_1() throws Exception {
		//('do create branch with valid, should succeed')
		click_create_new_branch();
		String branch = generate_string(5).toUpperCase();
		String code = generate_int(5).toString();
		fill_new_branch(branch, code);
		click_save_branch();	
		Branches.add(branch);
		//('check new branch created successfully, should succeed')
		assertTrue(search_branch(branch));
	}	

	@Test
	public void Branch_2() throws Exception {
		//('click create new branch, should succeed')
		click_create_new_branch();
		//('validate create new branch requirements, should succeed')
		assertTrue(element_is_readonly(BranchPage.new_branch_id));
		assertTrue(element_is_enabled(BranchPage.new_branch_name));
		assertTrue(element_is_displayed(BranchPage.new_branch_name_req));
	    assertTrue(element_is_enabled(BranchPage.new_branch_code));
	    assertTrue(element_is_displayed(BranchPage.new_branch_code_req));
	    //('do create branch with one character, should succeed')
	    String branch = generate_string(1).toUpperCase();
	    String code = generate_int(1).toString();
	    fill_new_branch(branch, code);
	    //('validate create new branch parameters, should succeed')
		assertFalse(element_is_displayed(BranchPage.new_branch_name_req));
		assertTrue(element_is_displayed(BranchPage.new_branch_name_invalid_length));
		assertFalse(element_is_displayed(BranchPage.new_branch_code_req));
		assertTrue(element_is_displayed(BranchPage.new_branch_code_invalid_length));
		//('proper error message, should succeed')
		String logged_text = get_text_filed(BranchPage.new_branch_name_invalid_length);
		String expected_text = "This field is required to be at least 5 characters.";
		assertEquals(logged_text, expected_text);
		logged_text = get_text_filed(BranchPage.new_branch_code_invalid_length);
		expected_text = "This field is required to be at least 2 characters.";
		assertEquals(logged_text, expected_text);
		assertFalse(element_is_enabled(BranchPage.save_branch_button));
		//('do create branch with invalid characters, should succeed')
		branch = generate_int(5).toString();
		code = generate_string(2);
		fill_new_branch(branch, code);
		//('validate create new branch parameters, should succeed')
	    assertFalse(element_is_displayed(BranchPage.new_branch_name_invalid_length));
	    assertTrue(element_is_displayed(BranchPage.new_branch_name_invalid));
	    assertFalse(element_is_displayed(BranchPage.new_branch_code_invalid_length));
	    assertTrue(element_is_displayed(BranchPage.new_branch_code_invalid));
	    assertFalse(element_is_enabled(BranchPage.save_branch_button));
	    //('proper error message, should succeed')
		logged_text = get_text_filed(BranchPage.new_branch_name_invalid);
		expected_text = "This field should follow pattern ^[a-zA-Z\\s]*$.";
		assertEquals(logged_text, expected_text);
		logged_text = get_text_filed(BranchPage.new_branch_code_invalid);
		expected_text = "This field should follow pattern ^[A-Z0-9]*$.";
		assertEquals(logged_text, expected_text);
		//('do create branch with invalid max length, should succeed')
		branch = generate_string(21).toUpperCase();
		code = generate_int(11).toString();
		fill_new_branch(branch, code);
		//('validate create new branch parameters, should succeed')
	    assertFalse(element_is_displayed(BranchPage.new_branch_name_invalid));
	    assertTrue(element_is_displayed(BranchPage.new_branch_name_invalid_maxlength));
	    assertFalse(element_is_displayed(BranchPage.new_branch_code_invalid));
	    assertTrue(element_is_displayed(BranchPage.new_branch_code_invalid_maxlength));
	    assertFalse(element_is_enabled(BranchPage.save_branch_button));
	    //('proper error message, should succeed')
		logged_text = get_text_filed(BranchPage.new_branch_name_invalid_maxlength);
		expected_text = "This field cannot be longer than 20 characters.";
		assertEquals(logged_text, expected_text);
		logged_text = get_text_filed(BranchPage.new_branch_code_invalid_maxlength);
		expected_text = "This field cannot be longer than 10 characters.";
		assertEquals(logged_text, expected_text);
		//('do create branch with valid, should succeed')
		branch = generate_string(5).toUpperCase();
		code = generate_int(5).toString();
		fill_new_branch(branch, code);
		assertFalse(element_is_displayed(BranchPage.new_branch_name_invalid_maxlength));
		assertFalse(element_is_displayed(BranchPage.new_branch_code_invalid_maxlength));
		//('click cancel branch, should succeed')
		click_btn(BranchPage.cancel_branch_button);
		//('check new branch not created, should succeed')
		assertFalse(search_branch(branch));
	}		
	
	@Test
	public void Branch_3() throws Exception {
		//('do create branch with valid, should succeed')
		click_create_new_branch();
		String branch = generate_string(5).toUpperCase();
		String code = generate_int(5).toString();
		fill_new_branch(branch, code);
		click_save_branch();	
		Branches.add(branch);
		//('check new branch created successfully, should succeed')
		assertTrue(search_branch(branch));
		//('view branch with name, should succeed')
		assertTrue(view_branch(branch));
		assertTrue(element_is_readonly(BranchPage.search_branch_view_name));
		assertTrue(element_is_readonly(BranchPage.search_branch_view_code));
		String logged_text = get_value_filed(BranchPage.search_branch_view_name);
		assertEquals(logged_text, branch);
		logged_text = get_value_filed(BranchPage.search_branch_view_code);
		assertEquals(logged_text, code);
		click_btn(BranchPage.view_back_button);
		//('delete branch, should succeed')
		delete_branch(branch);
		assertFalse(search_branch(branch));
		Branches.remove(branch);
	}
	
	@Test
	public void Branch_4() throws Exception {
		//('do create branch with valid, should succeed')
		click_create_new_branch();
		String branch = generate_string(5).toUpperCase();
		String code = generate_int(5).toString();
		fill_new_branch(branch, code);
		click_save_branch();	
		Branches.add(branch);
		//('check new branch created successfully, should succeed')
		assertTrue(search_branch(branch));
		//('edit branch with valid, should succeed')
		String new_branch = generate_string(5).toUpperCase();
		String new_code = generate_int(5).toString();
		edit_branch(branch);
		edit_created_branch(new_branch, new_code);
		click_btn(BranchPage.save_edit_branch_button);
		//('check new branch updated successfully, should succeed')
		assertFalse(search_branch(branch));
		Branches.remove(branch);
		assertTrue(search_branch(new_branch));
		Branches.add(new_branch);
		//('delete branch, should succeed')
		delete_branch(new_branch);
		assertFalse(search_branch(new_branch));
		Branches.remove(new_branch);
	}
	
	@Test
	public void Branch_5() throws Exception {
		//('do create branch with valid, should succeed')
		click_create_new_branch();
		String branch = generate_string(5).toUpperCase();
		String code = generate_int(5).toString();
		fill_new_branch(branch, code);
		click_save_branch();	
		Branches.add(branch);
		//('check new branch created successfully, should succeed')
		assertTrue(search_branch(branch));
		//('validate create new branch requirements, should succeed')
	    edit_branch(branch);
	    edit_created_branch("", "");
	    assertTrue(element_is_displayed(BranchPage.new_branch_name_req));
	    assertTrue(element_is_displayed(BranchPage.new_branch_code_req));
	    //('edit branch with one character, should succeed')
		String new_branch = generate_string(1).toUpperCase();
		String new_code = generate_int(1).toString();
	    edit_created_branch(new_branch, new_code);
	    //('validate create new branch parameters, should succeed')
		assertFalse(element_is_displayed(BranchPage.new_branch_name_req));
		assertTrue(element_is_displayed(BranchPage.new_branch_name_invalid_length));
		assertFalse(element_is_displayed(BranchPage.new_branch_code_req));
		assertTrue(element_is_displayed(BranchPage.new_branch_code_invalid_length));
	    //('proper error message, should succeed')
		String logged_text = get_text_filed(BranchPage.new_branch_name_invalid_length);
		String expected_text = "This field is required to be at least 5 characters.";
		assertEquals(logged_text, expected_text);
		logged_text = get_text_filed(BranchPage.new_branch_code_invalid_length);
		expected_text = "This field is required to be at least 2 characters.";
		assertEquals(logged_text, expected_text);
		assertFalse(element_is_enabled(BranchPage.save_branch_button));
		//('edit branch with invalid characters, should succeed')
		new_branch = generate_int(5).toString();
		new_code = generate_string(2);
	    edit_created_branch(new_branch, new_code);
	    //('validate create new branch parameters, should succeed')
	    assertFalse(element_is_displayed(BranchPage.new_branch_name_invalid_length));
	    assertTrue(element_is_displayed(BranchPage.new_branch_name_invalid));
	    assertFalse(element_is_displayed(BranchPage.new_branch_code_invalid_length));
	    assertTrue(element_is_displayed(BranchPage.new_branch_code_invalid));
	    assertFalse(element_is_enabled(BranchPage.save_branch_button));
	    //('proper error message, should succeed')
		logged_text = get_text_filed(BranchPage.new_branch_name_invalid);
		expected_text = "This field should follow pattern ^[a-zA-Z\\s]*$.";
		assertEquals(logged_text, expected_text);
		logged_text = get_text_filed(BranchPage.new_branch_code_invalid);
		expected_text = "This field should follow pattern ^[A-Z0-9]*$.";
		assertEquals(logged_text, expected_text);
		//('edit branch with invalid max length, should succeed')
		new_branch = generate_string(21).toUpperCase();
		new_code = generate_int(11).toString();
	    edit_created_branch(new_branch, new_code);
	    //('validate create new branch parameters, should succeed')
	    assertFalse(element_is_displayed(BranchPage.new_branch_name_invalid));
	    assertTrue(element_is_displayed(BranchPage.new_branch_name_invalid_maxlength));
	    assertFalse(element_is_displayed(BranchPage.new_branch_code_invalid));
	    assertTrue(element_is_displayed(BranchPage.new_branch_code_invalid_maxlength));
	    assertFalse(element_is_enabled(BranchPage.save_branch_button));
	    //('proper error message, should succeed')
		logged_text = get_text_filed(BranchPage.new_branch_name_invalid_maxlength);
		expected_text = "This field cannot be longer than 20 characters.";
		assertEquals(logged_text, expected_text);
		logged_text = get_text_filed(BranchPage.new_branch_code_invalid_maxlength);
		expected_text = "This field cannot be longer than 10 characters.";
		assertEquals(logged_text, expected_text);
		//('edit branch with valid, should succeed')
		new_branch = generate_string(5).toUpperCase();
		new_code = generate_int(5).toString();
	    edit_created_branch(new_branch, new_code);
		assertFalse(element_is_displayed(BranchPage.new_branch_name_invalid_maxlength));
		assertFalse(element_is_displayed(BranchPage.new_branch_code_invalid_maxlength));
		//('click cancel branch, should succeed')
		click_btn(BranchPage.cancel_edit_branch_button);
		//('check new branch not updated, should succeed')
		assertFalse(search_branch(new_branch));
	}
	
	@Test
	public void Branch_6() throws Exception {
		//('do create new branch, should succeed')
		click_create_new_branch();
		String branch = generate_string(5).toUpperCase();
		String code = generate_int(5).toString();
		fill_new_branch(branch, code);
		click_save_branch();	
		Branches.add(branch);
		//('search new branch, should succeed')
		assertTrue(search_branch(branch));
		//('delete branch, should succeed')
		delete_branch(branch);
		//('search new branch, should fail')
		assertFalse(search_branch(branch));
		Branches.remove(branch);
	}
	
	@Test
	public void Branch_7() throws Exception {
		//('do create new branch, should succeed')
		click_create_new_branch();
		String branch = generate_string(5).toUpperCase();
		String code = generate_int(5).toString();
		fill_new_branch(branch, code);
		click_save_branch();	
		Branches.add(branch);
		//('search invalid branch, should fail')
		assertFalse(search_branch(generate_string(1000).toUpperCase()));
		assertFalse(search_branch(generate_int(1000)));
		assertFalse(search_branch("+_=-)(*&^#!~`{}[];',.<>/"));
		assertTrue(search_branch(branch));
		//('delete branch, should succeed')
		delete_branch(branch);
		//('search invalid branch, should fail')
		assertFalse(search_branch(branch));
		Branches.remove(branch);
	}

	@Test
	public void Branch_8() throws Exception {
		//('do create new branch1, should succeed')
		String first_branch = generate_string(5).toUpperCase();
		String code = generate_int(5).toString();
		int count = 0;
		int first_counter = 2;
		while (count < first_counter){
			click_create_new_branch();
			fill_new_branch(first_branch, code);
			click_save_branch();	
			Branches.add(first_branch);
			//('check new branch created successfully, should succeed')
			assertTrue(search_branch(first_branch));
			count++;
		}
		//('search new branch1, should succeed')
		assertTrue(search_branch(first_branch));
		assertEquals(get_table_count(BranchPage.search_branch_table), first_counter);
		//('do create new branch2, should succeed')
		String second_branch = generate_string(5).toUpperCase();
		count = 0;
		int second_counter = 3;
		while (count < second_counter){
			click_create_new_branch();
			fill_new_branch(second_branch, code);
			click_save_branch();	
			Branches.add(second_branch);
			//('check new branch created successfully, should succeed')
			assertTrue(search_branch(second_branch));
			count++;
		}
		//('search new branch2, should succeed')
		assertTrue(search_branch(second_branch));
		assertEquals(get_table_count(BranchPage.search_branch_table), second_counter);
		//('search new branch1, should succeed')
		assertTrue(search_branch(first_branch));
		assertEquals(get_table_count(BranchPage.search_branch_table), first_counter);
		//('search new branch2, should succeed')
		assertTrue(search_branch(second_branch));
		assertEquals(get_table_count(BranchPage.search_branch_table), second_counter);
	}
	
	
}
