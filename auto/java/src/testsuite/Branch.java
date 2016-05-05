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
		click_create_new_branch();
		String branch = generate_string(5).toUpperCase();
		String code = generate_int(5).toString();
		fill_new_branch(branch, code);
		click_save_branch();	
		Branches.add(branch);
		assertTrue(search_branch(branch));
	}	

	@Test
	public void Branch_2() throws Exception {
		click_create_new_branch();
		assertTrue(element_is_readonly(BranchPage.new_branch_id));
		assertTrue(element_is_enabled(BranchPage.new_branch_name));
		assertTrue(element_is_displayed(BranchPage.new_branch_name_req));
	    assertTrue(element_is_enabled(BranchPage.new_branch_code));
	    assertTrue(element_is_displayed(BranchPage.new_branch_code_req));
	    
	    String branch = generate_string(1).toUpperCase();
	    String code = generate_int(1).toString();
	    fill_new_branch(branch, code);
		assertFalse(element_is_displayed(BranchPage.new_branch_name_req));
		assertTrue(element_is_displayed(BranchPage.new_branch_name_invalid_length));
		assertFalse(element_is_displayed(BranchPage.new_branch_code_req));
		assertTrue(element_is_displayed(BranchPage.new_branch_code_invalid_length));
		String logged_text = get_text_filed(BranchPage.new_branch_name_invalid_length);
		String expected_text = "This field is required to be at least 5 characters.";
		assertEquals(logged_text, expected_text);
		logged_text = get_text_filed(BranchPage.new_branch_code_invalid_length);
		expected_text = "This field is required to be at least 2 characters.";
		assertEquals(logged_text, expected_text);
		assertFalse(element_is_enabled(BranchPage.save_branch_button));
		
		branch = generate_int(5).toString();
		code = generate_string(2);
		fill_new_branch(branch, code);
	    assertFalse(element_is_displayed(BranchPage.new_branch_name_invalid_length));
	    assertTrue(element_is_displayed(BranchPage.new_branch_name_invalid));
	    assertFalse(element_is_displayed(BranchPage.new_branch_code_invalid_length));
	    assertTrue(element_is_displayed(BranchPage.new_branch_code_invalid));
	    assertFalse(element_is_enabled(BranchPage.save_branch_button));
		logged_text = get_text_filed(BranchPage.new_branch_name_invalid);
		expected_text = "This field should follow pattern ^[a-zA-Z\\s]*$.";
		assertEquals(logged_text, expected_text);
		logged_text = get_text_filed(BranchPage.new_branch_code_invalid);
		expected_text = "This field should follow pattern ^[A-Z0-9]*$.";
		assertEquals(logged_text, expected_text);
		
		branch = generate_string(21).toUpperCase();
		code = generate_int(11).toString();
		fill_new_branch(branch, code);
	    assertFalse(element_is_displayed(BranchPage.new_branch_name_invalid));
	    assertTrue(element_is_displayed(BranchPage.new_branch_name_invalid_maxlength));
	    assertFalse(element_is_displayed(BranchPage.new_branch_code_invalid));
	    assertTrue(element_is_displayed(BranchPage.new_branch_code_invalid_maxlength));
	    assertFalse(element_is_enabled(BranchPage.save_branch_button));
		logged_text = get_text_filed(BranchPage.new_branch_name_invalid_maxlength);
		expected_text = "This field cannot be longer than 20 characters.";
		assertEquals(logged_text, expected_text);
		logged_text = get_text_filed(BranchPage.new_branch_code_invalid_maxlength);
		expected_text = "This field cannot be longer than 10 characters.";
		assertEquals(logged_text, expected_text);
		
		branch = generate_string(5).toUpperCase();
		code = generate_int(5).toString();
		fill_new_branch(branch, code);
		assertFalse(element_is_displayed(BranchPage.new_branch_name_invalid_maxlength));
		assertFalse(element_is_displayed(BranchPage.new_branch_code_invalid_maxlength));
		click_btn(BranchPage.cancel_branch_button);
		assertFalse(search_branch(branch));
	}		
	
	@Test
	public void Branch_3() throws Exception {
		click_create_new_branch();
		String branch = generate_string(5).toUpperCase();
		String code = generate_int(5).toString();
		fill_new_branch(branch, code);
		click_save_branch();	
		Branches.add(branch);
		assertTrue(search_branch(branch));
		assertTrue(view_branch(branch));
		assertTrue(element_is_readonly(BranchPage.search_branch_view_name));
		assertTrue(element_is_readonly(BranchPage.search_branch_view_code));
		String logged_text = get_value_filed(BranchPage.search_branch_view_name);
		assertEquals(logged_text, branch);
		logged_text = get_value_filed(BranchPage.search_branch_view_code);
		assertEquals(logged_text, code);
		click_btn(BranchPage.view_back_button);
		delete_branch(branch);
		assertFalse(search_branch(branch));
		Branches.remove(branch);
	}
	
	@Test
	public void Branch_4() throws Exception {
		click_create_new_branch();
		String branch = generate_string(5).toUpperCase();
		String code = generate_int(5).toString();
		fill_new_branch(branch, code);
		click_save_branch();	
		Branches.add(branch);
		assertTrue(search_branch(branch));
		
		String new_branch = generate_string(5).toUpperCase();
		String new_code = generate_int(5).toString();
		edit_branch(branch);
		edit_created_branch(new_branch, new_code);
		click_btn(BranchPage.save_edit_branch_button);
		assertFalse(search_branch(branch));
		Branches.remove(branch);
		assertTrue(search_branch(new_branch));
		Branches.add(new_branch);
		delete_branch(new_branch);
		assertFalse(search_branch(new_branch));
		Branches.remove(new_branch);
	}
	
	@Test
	public void Branch_5() throws Exception {
		click_create_new_branch();
		String branch = generate_string(5).toUpperCase();
		String code = generate_int(5).toString();
		fill_new_branch(branch, code);
		click_save_branch();	
		Branches.add(branch);
		assertTrue(search_branch(branch));
	    
		String new_branch = generate_string(1).toUpperCase();
		String new_code = generate_int(1).toString();
	    edit_branch(branch);
	    edit_created_branch(new_branch, new_code);
		assertFalse(element_is_displayed(BranchPage.new_branch_name_req));
		assertTrue(element_is_displayed(BranchPage.new_branch_name_invalid_length));
		assertFalse(element_is_displayed(BranchPage.new_branch_code_req));
		assertTrue(element_is_displayed(BranchPage.new_branch_code_invalid_length));
		String logged_text = get_text_filed(BranchPage.new_branch_name_invalid_length);
		String expected_text = "This field is required to be at least 5 characters.";
		assertEquals(logged_text, expected_text);
		logged_text = get_text_filed(BranchPage.new_branch_code_invalid_length);
		expected_text = "This field is required to be at least 2 characters.";
		assertEquals(logged_text, expected_text);
		assertFalse(element_is_enabled(BranchPage.save_branch_button));
		
		new_branch = generate_int(5).toString();
		new_code = generate_string(2);
	    edit_created_branch(new_branch, new_code);
	    assertFalse(element_is_displayed(BranchPage.new_branch_name_invalid_length));
	    assertTrue(element_is_displayed(BranchPage.new_branch_name_invalid));
	    assertFalse(element_is_displayed(BranchPage.new_branch_code_invalid_length));
	    assertTrue(element_is_displayed(BranchPage.new_branch_code_invalid));
	    assertFalse(element_is_enabled(BranchPage.save_branch_button));
		logged_text = get_text_filed(BranchPage.new_branch_name_invalid);
		expected_text = "This field should follow pattern ^[a-zA-Z\\s]*$.";
		assertEquals(logged_text, expected_text);
		logged_text = get_text_filed(BranchPage.new_branch_code_invalid);
		expected_text = "This field should follow pattern ^[A-Z0-9]*$.";
		assertEquals(logged_text, expected_text);
		
		new_branch = generate_string(21).toUpperCase();
		new_code = generate_int(11).toString();
	    edit_created_branch(new_branch, new_code);
	    assertFalse(element_is_displayed(BranchPage.new_branch_name_invalid));
	    assertTrue(element_is_displayed(BranchPage.new_branch_name_invalid_maxlength));
	    assertFalse(element_is_displayed(BranchPage.new_branch_code_invalid));
	    assertTrue(element_is_displayed(BranchPage.new_branch_code_invalid_maxlength));
	    assertFalse(element_is_enabled(BranchPage.save_branch_button));
		logged_text = get_text_filed(BranchPage.new_branch_name_invalid_maxlength);
		expected_text = "This field cannot be longer than 20 characters.";
		assertEquals(logged_text, expected_text);
		logged_text = get_text_filed(BranchPage.new_branch_code_invalid_maxlength);
		expected_text = "This field cannot be longer than 10 characters.";
		assertEquals(logged_text, expected_text);
		
		new_branch = generate_string(5).toUpperCase();
		new_code = generate_int(5).toString();
	    edit_created_branch(new_branch, new_code);
		assertFalse(element_is_displayed(BranchPage.new_branch_name_invalid_maxlength));
		assertFalse(element_is_displayed(BranchPage.new_branch_code_invalid_maxlength));
		click_btn(BranchPage.cancel_edit_branch_button);
		assertFalse(search_branch(new_branch));
	}
	
	@Test
	public void Branch_6() throws Exception {
		click_create_new_branch();
		String branch = generate_string(5).toUpperCase();
		String code = generate_int(5).toString();
		fill_new_branch(branch, code);
		click_save_branch();	
		Branches.add(branch);
		assertTrue(search_branch(branch));
		delete_branch(branch);
		assertFalse(search_branch(branch));
		Branches.remove(branch);
	}
	
	@Test
	public void Branch_7() throws Exception {
		click_create_new_branch();
		String branch = generate_string(5).toUpperCase();
		String code = generate_int(5).toString();
		fill_new_branch(branch, code);
		click_save_branch();	
		Branches.add(branch);
		assertFalse(search_branch(generate_string(1000).toUpperCase()));
		assertTrue(search_branch(branch));
		delete_branch(branch);
		assertFalse(search_branch(branch));
		Branches.remove(branch);
	}

	@Test
	public void Branch_8() throws Exception {
		String first_branch = generate_string(5).toUpperCase();
		String code = generate_int(5).toString();
		int count = 0;
		int first_counter = 2;
		while (count < first_counter){
			click_create_new_branch();
			fill_new_branch(first_branch, code);
			click_save_branch();	
			Branches.add(first_branch);
			assertTrue(search_branch(first_branch));
			count++;
		}
		
		String second_branch = generate_string(5).toUpperCase();
		count = 0;
		int second_counter = 3;
		while (count < second_counter){
			click_create_new_branch();
			fill_new_branch(second_branch, code);
			click_save_branch();	
			Branches.add(second_branch);
			assertTrue(search_branch(second_branch));
			count++;
		}
		
		assertTrue(search_branch(first_branch));
		assertEquals(get_table_count(BranchPage.search_branch_table), first_counter);
		assertTrue(search_branch(second_branch));
		assertEquals(get_table_count(BranchPage.search_branch_table), second_counter);
	}
	
	
}
