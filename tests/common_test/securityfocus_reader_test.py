import unittest
from openwebvulndb.common.securityfocus.securityfocusparsers import InfoTabParser, ReferenceTabParser
from fixtures import file_path
from openwebvulndb.common.securityfocus.securityfocus import SecurityFocusReader
from openwebvulndb.common.storage import Storage
import json
import os


class SecurityFocusReaderTest(unittest.TestCase):

    def test_add_vuln_73931_to_database(self):
        bugtraq_id = "73931"
        plugin_path = "plugins/wassup"
        # Remove the vuln entry file if it already exists to ensure the validity of the test.
        try:
            os.remove(file_path(__file__, "../../data/" + plugin_path + "/vuln-security-focus.json"))
        except FileNotFoundError:
            pass
        entry = dict()
        entry['id'] = bugtraq_id
        info_parser = InfoTabParser()
        info_parser.set_html_page(file_path(__file__, "samples/" + bugtraq_id + "/info_tab.html"))
        entry['info_parser'] = info_parser
        references_parser = ReferenceTabParser()
        references_parser.set_html_page(file_path(__file__, "samples/" + bugtraq_id + "/references_tab.html"))
        entry['references_parser'] = references_parser
        storage = Storage(base_path=file_path(__file__, "../../data"))
        reader = SecurityFocusReader(storage=storage)
        reader.read_one(entry)
        vuln_entry_file = open(file_path(__file__, "../../data/" + plugin_path + "/vuln-security-focus.json"), "rt")
        json_vuln_entry = json.load(vuln_entry_file)
        self.assertEqual(json_vuln_entry['key'], plugin_path)
        self.assertEqual(json_vuln_entry['producer'], "security-focus")
        vuln_list = json_vuln_entry['vulnerabilities']
        vuln = vuln_list[0]
        self.assertEqual(vuln['id'], bugtraq_id)
        self.assertEqual(vuln['title'], "WordPress WassUp Plugin 'main.php' Cross Site Scripting Vulnerability")
        self.assertEqual(vuln['reported_type'], "Input Validation Error")
        reference = vuln['references'][0]
        self.assertEqual(reference['type'], "Bugtraq-ID")
        self.assertEqual(reference['id'], bugtraq_id)
        vuln_entry_file.close()

    def test_add_vuln_73931_to_database_allow_override(self):
        """Test if a more recent vuln entry allow to override an old one."""
        bugtraq_id = "73931"
        plugin_path = "plugins/wassup"
        entry = dict()
        entry['id'] = bugtraq_id
        info_parser = InfoTabParser()
        info_parser.set_html_page(file_path(__file__, "samples/" + bugtraq_id + "/info_tab_fake_update_date.html"))
        entry['info_parser'] = info_parser
        references_parser = ReferenceTabParser()
        references_parser.set_html_page(file_path(__file__, "samples/" + bugtraq_id + "/references_tab.html"))
        entry['references_parser'] = references_parser
        storage = Storage(base_path=file_path(__file__, "../../data"))
        reader = SecurityFocusReader(storage=storage)
        reader.read_one(entry)
        try:
            vuln_entry_file = open(file_path(__file__, "../../data/" + plugin_path + "/vuln-security-focus.json"), "rt")
        except FileNotFoundError:
            self.skipTest("The previous test has failed, so this test can't  be done.")
        json_vuln_entry = json.load(vuln_entry_file)
        self.assertEqual(json_vuln_entry['key'], plugin_path)
        self.assertEqual(json_vuln_entry['producer'], "security-focus")
        vuln_list = json_vuln_entry['vulnerabilities']
        vuln = vuln_list[0]
        self.assertEqual(vuln['id'], bugtraq_id)
        self.assertEqual(vuln['title'], "WordPress WassUp Plugin 'main.php' Fake Title")
        self.assertEqual(vuln['reported_type'], "Random Vuln Class")
        reference = vuln['references'][0]
        self.assertEqual(reference['type'], "Bugtraq-ID")
        self.assertEqual(reference['id'], bugtraq_id)
        vuln_entry_file.close()

    def test_add_vuln_73931_to_database_no_override(self):
        """Test if a less recent vuln entry can't override a newer one."""
        bugtraq_id = "73931"
        plugin_path = "plugins/wassup"
        entry = dict()
        entry['id'] = bugtraq_id
        info_parser = InfoTabParser()
        info_parser.set_html_page(file_path(__file__, "samples/" + bugtraq_id + "/info_tab_older_update_date.html"))
        entry['info_parser'] = info_parser
        references_parser = ReferenceTabParser()
        references_parser.set_html_page(file_path(__file__, "samples/" + bugtraq_id + "/references_tab.html"))
        entry['references_parser'] = references_parser
        storage = Storage(base_path=file_path(__file__, "../../data"))
        reader = SecurityFocusReader(storage=storage)
        reader.read_one(entry)
        try:
            vuln_entry_file = open(file_path(__file__, "../../data/" + plugin_path + "/vuln-security-focus.json"), "rt")
        except FileNotFoundError:
            self.skipTest("The previous test has failed, so this test can't  be done.")
        json_vuln_entry = json.load(vuln_entry_file)
        self.assertEqual(json_vuln_entry['key'], plugin_path)
        self.assertEqual(json_vuln_entry['producer'], "security-focus")
        vuln_list = json_vuln_entry['vulnerabilities']
        vuln = vuln_list[0]
        self.assertEqual(vuln['id'], bugtraq_id)
        self.assertEqual(vuln['title'], "WordPress WassUp Plugin 'main.php' Fake Title")
        self.assertEqual(vuln['reported_type'], "Random Vuln Class")
        reference = vuln['references'][0]
        self.assertEqual(reference['type'], "Bugtraq-ID")
        self.assertEqual(reference['id'], bugtraq_id)
        vuln_entry_file.close()

    def test_add_vuln_92077_to_database(self):
        bugtraq_id = "92077"
        plugin_path = "plugins/nofollow-links"
        # Remove the vuln entry file if it already exists to ensure the validity of the test.
        try:
            os.remove(file_path(__file__, "../../data/" + plugin_path + "/vuln-security-focus.json"))
        except FileNotFoundError:
            pass
        entry = dict()
        entry['id'] = bugtraq_id
        info_parser = InfoTabParser()
        info_parser.set_html_page(file_path(__file__, "samples/" + bugtraq_id + "/info_tab.html"))
        entry['info_parser'] = info_parser
        references_parser = ReferenceTabParser()
        references_parser.set_html_page(file_path(__file__, "samples/" + bugtraq_id + "/references_tab.html"))
        entry['references_parser'] = references_parser
        storage = Storage(base_path=file_path(__file__, "../../data"))
        reader = SecurityFocusReader(storage=storage)
        reader.read_one(entry)
        vuln_entry_file = open(file_path(__file__, "../../data/" + plugin_path + "/vuln-security-focus.json"), "rt")
        json_vuln_entry = json.load(vuln_entry_file)
        self.assertEqual(json_vuln_entry['key'], plugin_path)
        self.assertEqual(json_vuln_entry['producer'], "security-focus")
        vuln_list = json_vuln_entry['vulnerabilities']
        vuln = vuln_list[0]
        self.assertEqual(vuln['id'], bugtraq_id)
        self.assertEqual(vuln['title'], "WordPress Nofollow Links Plugin 'nofollow-links.php' Cross Site Scripting Vulnerability")
        self.assertEqual(vuln['reported_type'], "Input Validation Error")
        reference = vuln['references'][0]
        self.assertEqual(reference['type'], "Bugtraq-ID")
        self.assertEqual(reference['id'], bugtraq_id)
        reference = vuln['references'][1]
        self.assertEqual(reference['type'], "cve")
        self.assertEqual(reference['id'], "2016-4833")
        vuln_entry_file.close()

    def test_add_vuln_92572_to_database(self):
        bugtraq_id = "92572"
        key = "wordpress"
        # Remove the vuln entry file if it already exists to ensure the validity of the test.
        try:
            os.remove(file_path(__file__, "../../data/" + key + "/vuln-security-focus.json"))
        except FileNotFoundError:
            pass
        entry = dict()
        entry['id'] = bugtraq_id
        info_parser = InfoTabParser()
        info_parser.set_html_page(file_path(__file__, "samples/" + bugtraq_id + "/info_tab.html"))
        entry['info_parser'] = info_parser
        references_parser = ReferenceTabParser()
        references_parser.set_html_page(file_path(__file__, "samples/" + bugtraq_id + "/references_tab.html"))
        entry['references_parser'] = references_parser
        storage = Storage(base_path=file_path(__file__, "../../data"))
        reader = SecurityFocusReader(storage=storage)
        reader.read_one(entry)
        vuln_entry_file = open(file_path(__file__, "../../data/" + key + "/vuln-security-focus.json"), "rt")
        json_vuln_entry = json.load(vuln_entry_file)
        self.assertEqual(json_vuln_entry['key'], key)
        self.assertEqual(json_vuln_entry['producer'], "security-focus")
        vuln_list = json_vuln_entry['vulnerabilities']
        vuln = vuln_list[0]
        self.assertEqual(vuln['id'], bugtraq_id)
        self.assertEqual(vuln['title'], "WordPress CVE-2016-6897 Cross Site Request Forgery Vulnerability")
        self.assertEqual(vuln['reported_type'], "Input Validation Error")
        reference = vuln['references'][0]
        self.assertEqual(reference['type'], "Bugtraq-ID")
        self.assertEqual(reference['id'], bugtraq_id)
        reference = vuln['references'][1]
        self.assertEqual(reference['type'], "cve")
        self.assertEqual(reference['id'], "2016-6897")
        vuln_entry_file.close()

    def test_add_vuln_92841_to_database(self):
        bugtraq_id = "92841"
        key = "wordpress"
        entry = dict()
        entry['id'] = bugtraq_id
        info_parser = InfoTabParser()
        info_parser.set_html_page(file_path(__file__, "samples/" + bugtraq_id + "/info_tab.html"))
        entry['info_parser'] = info_parser
        references_parser = ReferenceTabParser()
        references_parser.set_html_page(file_path(__file__, "samples/" + bugtraq_id + "/references_tab.html"))
        entry['references_parser'] = references_parser
        storage = Storage(base_path=file_path(__file__, "../../data"))
        reader = SecurityFocusReader(storage=storage)
        reader.read_one(entry)
        try:  # The file should already exist because of the previous test. This vuln should be append to the existing file.
            vuln_entry_file = open(file_path(__file__, "../../data/" + key + "/vuln-security-focus.json"), "rt")
        except FileNotFoundError:
            self.skipTest("Previous test has failed, need a file from the previous test for this test.")  # If the file is not present, skip the test.
        json_vuln_entry = json.load(vuln_entry_file)
        self.assertEqual(json_vuln_entry['key'], key)
        self.assertEqual(json_vuln_entry['producer'], "security-focus")
        vuln_list = json_vuln_entry['vulnerabilities']
        vuln = vuln_list[1]
        self.assertEqual(vuln['id'], bugtraq_id)
        self.assertEqual(vuln['title'], "WordPress Cross Site Scripting And Directory Traversal Vulnerabilities")
        self.assertEqual(vuln['reported_type'], "Input Validation Error")
        reference = vuln['references'][0]
        self.assertEqual(reference['type'], "Bugtraq-ID")
        self.assertEqual(reference['id'], bugtraq_id)
        vuln_entry_file.close()
