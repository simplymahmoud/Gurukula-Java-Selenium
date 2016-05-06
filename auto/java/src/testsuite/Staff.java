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
import framework.model.StaffPage;


public class Staff extends factory{

	
	List<String> Branches = new ArrayList<String>();
	List<String> Staffs = new ArrayList<String>();
	
	@Before
	public void test_setup() throws Exception {
		click_login();
		fill_login("admin", "admin");
		click_authenticat();
		click_entities_staff_menu();
	}

	@After
	public void test_teardown() throws Exception {
		for(String staff: Staffs){
			delete_staff(staff);
		}
		
		for(String branch: Branches){
			delete_branch(branch);
		}
	}	
	
	@Test
	public void Staff_1() throws Exception {
		//('do create staff without branch, should succeed')
		click_create_new_staff();
		String staff = generate_string(5);
		fill_new_staff(staff, "");
		click_save_staff();	
		Staffs.add(staff);
		//('check new staff created successfully, should succeed')
		assertTrue(search_staff(staff));
		//('do create branch with valid, should succeed')
		click_entities_branch_menu();
		click_create_new_branch();
		String branch = generate_string(5).toUpperCase();
		String code = generate_int(5).toString();
		fill_new_branch(branch, code);
		click_save_branch();	
		Branches.add(branch);
		//('check new staff created successfully, should succeed')
		assertTrue(search_branch(branch));
		//('do create staff with branch, should succeed')
		String new_staff = generate_string(5);
		click_entities_staff_menu();
		click_create_new_staff();
		fill_new_staff(new_staff, branch);
		click_save_staff();	
		Staffs.add(new_staff);
		//('check new staff created successfully, should succeed')
		assertTrue(search_staff(new_staff));
		assertTrue(search_staff(staff));
	}	
	

	@Test
	public void Staff_2() throws Exception {
		//('click create new staff, should succeed')
		click_create_new_staff();
		//('validate create new branch requirements, should succeed')
		assertTrue(element_is_readonly(StaffPage.new_staff_id));
		assertTrue(element_is_enabled(StaffPage.new_staff_name));
		assertTrue(element_is_displayed(StaffPage.new_staff_name_req));
		assertTrue(element_is_enabled(StaffPage.staff_dropdown));
	    //('do create staff with invalid characters, should succeed')
		String staff = generate_int(5).toString();
		fill_new_staff(staff, "");
		//('validate create new staff parameters, should succeed')
	    assertFalse(element_is_displayed(StaffPage.new_staff_name_req));
	    assertTrue(element_is_displayed(StaffPage.new_staff_name_invalid));
	    assertFalse(element_is_enabled(StaffPage.save_staff_button));
	    //('proper error message, should succeed')
		String logged_text = get_text_filed(StaffPage.new_staff_name_invalid);
		String expected_text = "This field should follow pattern ^[a-zA-Z\\s]*$.";
		assertEquals(logged_text, expected_text);
		//('do create staff with invalid max length, should succeed')
		staff = generate_string(51);
		fill_new_staff(staff, "");
		//('validate create new staff parameters, should succeed')
	    assertFalse(element_is_displayed(StaffPage.new_staff_name_invalid));
	    assertTrue(element_is_displayed(StaffPage.new_staff_name_invalid_maxlength));
	    assertFalse(element_is_enabled(StaffPage.save_staff_button));
	    //('proper error message, should succeed')
		logged_text = get_text_filed(StaffPage.new_staff_name_invalid_maxlength);
		expected_text = "This field cannot be longer than 50 characters.";
		assertEquals(logged_text, expected_text);
		//('do create staff with valid, should succeed')
		staff = generate_string(5);
		fill_new_staff(staff, "");
		assertFalse(element_is_displayed(StaffPage.new_staff_name_invalid_maxlength));
		click_save_staff();	
		Staffs.add(staff);
		assertTrue(search_staff(staff));
	}	
	
	@Test
	public void Staff_3() throws Exception {
		//('do create staff with valid, should succeed')
		click_create_new_staff();
		String staff = generate_string(5);
		fill_new_staff(staff, "");
		click_save_staff();	
		Staffs.add(staff);
		//('check new staff created successfully, should succeed')
		assertTrue(search_staff(staff));
		//('view staff with name, should succeed')
		assertTrue(view_staff(staff));
		assertTrue(element_is_readonly(StaffPage.search_staff_view_name));
		assertTrue(element_is_readonly(StaffPage.search_staff_view_branch));
		String logged_text = get_value_filed(StaffPage.search_staff_view_name);
		assertEquals(logged_text, staff);
		click_view_back_button();
		//('delete staff, should succeed')
		delete_staff(staff);
		assertFalse(search_staff(staff));
		Staffs.remove(staff);
	}

	@Test
	public void Staff_4() throws Exception {
		//('do create staff with valid, should succeed')
		click_create_new_staff();
		String staff = generate_string(5);
		fill_new_staff(staff, "");
		click_save_staff();	
		Staffs.add(staff);
		//('check new staff created successfully, should succeed')
		assertTrue(search_staff(staff));
		//('edit staff with valid, should succeed')
		String new_staff = generate_string(5);
		edit_staff(staff);
		edit_created_staff(new_staff);
		click_btn(StaffPage.save_edit_staff_button);
		//('check new staff updated successfully, should succeed')
		assertFalse(search_staff(staff));
		Staffs.remove(staff);
		assertTrue(search_staff(new_staff));
		Staffs.add(new_staff);
		//('delete staff, should succeed')
		delete_staff(new_staff);
		assertFalse(search_staff(new_staff));
		Staffs.remove(new_staff);
	}
	
	@Test
	public void Staff_5() throws Exception {
		//('do create staff with valid, should succeed')
		click_create_new_staff();
		String staff = generate_string(5);
		fill_new_staff(staff, "");
		click_save_staff();	
		Staffs.add(staff);
		//('check new staff created successfully, should succeed')
		assertTrue(search_staff(staff));
		//('validate create new staff requirements, should succeed')
		edit_staff(staff);
		edit_created_staff("");
		assertTrue(element_is_readonly(StaffPage.new_staff_id));
		assertTrue(element_is_enabled(StaffPage.new_staff_name));
		assertTrue(element_is_displayed(StaffPage.new_staff_name_req));
		assertTrue(element_is_enabled(StaffPage.staff_dropdown));
		//('edit staff with invalid characters, should succeed')
		String new_staff = generate_int(5).toString();
		edit_created_staff(new_staff);
	    assertFalse(element_is_displayed(StaffPage.new_staff_name_req));
	    assertTrue(element_is_displayed(StaffPage.new_staff_name_invalid));
	    assertFalse(element_is_enabled(StaffPage.save_staff_button));
	    //('proper error message, should succeed')
		String logged_text = get_text_filed(StaffPage.new_staff_name_invalid);
		String expected_text = "This field should follow pattern ^[a-zA-Z\\s]*$.";
		assertEquals(logged_text, expected_text);
		//('edit staff with invalid max length, should succeed')
		new_staff = generate_string(51);
		edit_created_staff(new_staff);
		//('validate create new staff parameters, should succeed')
	    assertFalse(element_is_displayed(StaffPage.new_staff_name_invalid));
	    assertTrue(element_is_displayed(StaffPage.new_staff_name_invalid_maxlength));
	    assertFalse(element_is_enabled(StaffPage.save_staff_button));
		logged_text = get_text_filed(StaffPage.new_staff_name_invalid_maxlength);
		//('proper error message, should succeed')
		expected_text = "This field cannot be longer than 50 characters.";
		assertEquals(logged_text, expected_text);
		//('edit staff with valid, should succeed')
		new_staff = generate_string(5);
		edit_created_staff(new_staff);
		assertFalse(element_is_displayed(StaffPage.new_staff_name_invalid_maxlength));
		//('click cancel staff, should succeed')
		click_btn(StaffPage.cancel_staff_button);
		//('check new staff not updated, should succeed')
		assertTrue(search_staff(staff));
		assertFalse(search_staff(new_staff));
	}
	
	@Test
	public void Staff_6() throws Exception {
		//('do create new staff, should succeed')
		click_create_new_staff();
		String staff = generate_string(5);
		fill_new_staff(staff, "");
		click_save_staff();	
		Staffs.add(staff);
		//('search new staff, should succeed')
		assertTrue(search_staff(staff));
		//('delete staff, should succeed')
		delete_staff(staff);
		//('search new staff, should fail')
		assertFalse(search_staff(staff));
		Staffs.remove(staff);
	}
	
	@Test
	public void Staff_7() throws Exception {
		//('do create new staff, should succeed')
		click_create_new_staff();
		String staff = generate_string(5);
		fill_new_staff(staff, "");
		click_save_staff();	
		Staffs.add(staff);
		//('search new staff, should succeed')
		assertTrue(search_staff(staff));
		//('search invalid staff, should fail')		
		assertFalse(search_staff(generate_string(1000).toUpperCase()));
		assertFalse(search_staff(generate_int(1000)));
		assertFalse(search_staff("+_=-)(*&^#!~`{}[];',.<>/"));
		//('delete staff, should succeed')
		delete_staff(staff);
		//('search invalid staff, should fail')
		assertFalse(search_staff(staff));
		Staffs.remove(staff);
	}
	
	@Test
	public void Staff_8() throws Exception {	
		//('create multiple staff with valid, should succeed')
		String staff = generate_string(5);
		int count = 0;
		int counter = 50;
		while (count < counter){
			click_create_new_staff();
			fill_new_staff(staff, "");
			click_save_staff();	
			Staffs.add(staff);
			count++;
		}
		//('check paging is working successfully, should succeed')
		assertTrue(element_is_displayed(StaffPage.staff_paging_first_page));
	    assertFalse(element_is_displayed(StaffPage.staff_paging_previos_page));
	    assertTrue(element_is_displayed(StaffPage.staff_paging_next_page));
	    assertTrue(element_is_displayed(StaffPage.staff_paging_last_page));
	    //('check paging size is 20 record per page, should succeed')
	    assertEquals(get_table_count(StaffPage.search_staff_table), 20);
	    
	    click_btn(StaffPage.staff_paging_next_page);
		assertTrue(element_is_displayed(StaffPage.staff_paging_first_page));
		assertTrue(element_is_displayed(StaffPage.staff_paging_previos_page));
	    assertTrue(element_is_displayed(StaffPage.staff_paging_next_page));
	    assertTrue(element_is_displayed(StaffPage.staff_paging_last_page));
	    //('check paging size is 20 record per page, should succeed')
	    assertEquals(get_table_count(StaffPage.search_staff_table), 20);
	    
	    click_btn(StaffPage.staff_paging_next_page);
		assertTrue(element_is_displayed(StaffPage.staff_paging_first_page));
		assertTrue(element_is_displayed(StaffPage.staff_paging_previos_page));
		assertFalse(element_is_displayed(StaffPage.staff_paging_next_page));
	    assertTrue(element_is_displayed(StaffPage.staff_paging_last_page));
	    //('check paging size is 10 record per page, should succeed')
	    assertEquals(get_table_count(StaffPage.search_staff_table), 10);
	    
	    click_btn(StaffPage.staff_paging_previos_page);
		assertTrue(element_is_displayed(StaffPage.staff_paging_first_page));
		assertTrue(element_is_displayed(StaffPage.staff_paging_previos_page));
	    assertTrue(element_is_displayed(StaffPage.staff_paging_next_page));
	    assertTrue(element_is_displayed(StaffPage.staff_paging_last_page));
	    //('check paging size is 20 record per page, should succeed')
	    assertEquals(get_table_count(StaffPage.search_staff_table), 20);
	    
	    click_btn(StaffPage.staff_paging_first_page);
		assertTrue(element_is_displayed(StaffPage.staff_paging_first_page));
		assertFalse(element_is_displayed(StaffPage.staff_paging_previos_page));
	    assertTrue(element_is_displayed(StaffPage.staff_paging_next_page));
	    assertTrue(element_is_displayed(StaffPage.staff_paging_last_page));
	    //('check paging size is 20 record per page, should succeed')
	    assertEquals(get_table_count(StaffPage.search_staff_table), 20);
	    
	    click_btn(StaffPage.staff_paging_last_page);
		assertTrue(element_is_displayed(StaffPage.staff_paging_first_page));
		assertTrue(element_is_displayed(StaffPage.staff_paging_previos_page));
		assertFalse(element_is_displayed(StaffPage.staff_paging_next_page));
	    assertTrue(element_is_displayed(StaffPage.staff_paging_last_page));
	    //('check paging size is 10 record per page, should succeed')
	    assertEquals(get_table_count(StaffPage.search_staff_table), 10);
	}
	
	@Test
	public void Staff_9() throws Exception {
		//('do create branch with valid, should succeed')
		click_entities_branch_menu();
		click_create_new_branch();
		String branch = generate_string(5).toUpperCase();
		String code = generate_int(5).toString();
		fill_new_branch(branch, code);
		click_save_branch();	
		Branches.add(branch);
		//('check new branch created successfully, should succeed')
		assertTrue(search_branch(branch));
		//('do create new staff with branch, should succeed')
		String staff = generate_string(5);
		click_entities_staff_menu();
		click_create_new_staff();
		fill_new_staff(staff, branch);
		click_save_staff();	
		Staffs.add(staff);
		//('search new staff, should succeed')
		assertTrue(search_staff(staff));
		//('try delete branch before staff, should fail')
		click_entities_branch_menu();
		delete_branch(branch);
		click_cancel_delete_branch();
		assertTrue(search_branch(branch));
		assertEquals(get_table_count(StaffPage.search_staff_table), 1);
		click_entities_staff_menu();
		
	}
	
	@Test
	public void Staff_10() throws Exception {	
		//('do create staff without branch, should succeed')
		click_entities_branch_menu();
		click_create_new_branch();
		String branch = generate_string(5).toUpperCase();
		String code = generate_int(5).toString();
		fill_new_branch(branch, code);
		click_save_branch();	
		Branches.add(branch);
		assertTrue(search_branch(branch));
		String staff = generate_string(5);
		click_entities_staff_menu();
		click_create_new_staff();
		fill_new_staff(staff, "");
		click_save_staff();	
		Staffs.add(staff);
		assertTrue(search_staff(staff));
		//('delete branch before staff, should succeed')
		click_entities_branch_menu();
		delete_branch(branch);
		assertFalse(search_branch(branch));
		Branches.remove(branch);
		click_entities_staff_menu();
	}
	
	@Test
	public void Staff_11() throws Exception {	
		//('do create new staff1, should succeed')
		String first_staff = generate_string(5);
		int count = 0;
		int first_counter = 2;
		while (count < first_counter){
			click_create_new_staff();
			fill_new_staff(first_staff, "");
			click_save_staff();	
			Staffs.add(first_staff);
			//('search new staff1, should succeed')
			assertTrue(search_staff(first_staff));
			count++;
		}
		//('search new staff1, should succeed')
		assertTrue(search_staff(first_staff));
		assertEquals(get_table_count(StaffPage.search_staff_table), first_counter);
		//('do create new staff2, should succeed')
		String second_staff = generate_string(5);
		count = 0;
		int second_counter = 3;
		while (count < second_counter){
			click_create_new_staff();
			fill_new_staff(second_staff, "");
			click_save_staff();	
			Staffs.add(second_staff);
			assertTrue(search_staff(second_staff));
			count++;
		}
		//('search new staff1, should succeed')
		assertTrue(search_staff(first_staff));
		assertEquals(get_table_count(StaffPage.search_staff_table), first_counter);
		//('search new staff2, should succeed')
		assertTrue(search_staff(second_staff));
		assertEquals(get_table_count(StaffPage.search_staff_table), second_counter);
	}
	
}
