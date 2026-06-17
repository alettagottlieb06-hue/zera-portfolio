import flet as ft
import os

def main(page: ft.Page):
    page.title = "Welcome To My Portfolio"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO
    
    # --- FIXED: Corrected PascalCase for Colors ---
    PRIMARY_COLOR = ft.Colors.BLUE_400
    BG_CARD_COLOR = ft.Colors.SURFACE_VARIANT

    # --- Navigation Event Handlers ---
    def handle_menu_click(e):
        page.drawer.open = True
        page.drawer.update()

    def handle_drawer_change(e):
        page.drawer.open = False
        page.drawer.update()
        
        index = e.control.selected_index
        if index == 0:
            page.scroll_to(key="aboutme", duration=800, curve=ft.AnimationCurve.EASE_OUT)
        elif index == 1:
            page.scroll_to(key="timeline", duration=800, curve=ft.AnimationCurve.EASE_OUT)
        elif index == 2:
            page.scroll_to(key="blog", duration=800, curve=ft.AnimationCurve.EASE_OUT)
        elif index == 3:
            page.scroll_to(key="matlab", duration=800, curve=ft.AnimationCurve.EASE_OUT)
        elif index == 4:
            page.scroll_to(key="commit", duration=800, curve=ft.AnimationCurve.EASE_OUT)
        elif index == 5:
            page.scroll_to(key="pr", duration=800, curve=ft.AnimationCurve.EASE_OUT)

    def handle_admin_click(e):
        page.snack_bar = ft.SnackBar(ft.Text("Navigating to Admin Console..."))
        page.snack_bar.open = True
        page.update()

    def handle_message_click(e):
        page.snack_bar = ft.SnackBar(ft.Text("Opening Messages/Contact Form..."))
        page.snack_bar.open = True
        page.update()

    def open_github(e):
        page.launch_url("https://github.com/waardeakawa-sys/UNAM-I36991CP-GROUP-10-TOOLBOX/pulls")

    # Dynamic interactive asset cards
    def create_certificate_card(title, file_name):
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Icon(ft.icons.PICTURE_AS_PDF_ROUNDED, size=40, color=ft.Colors.RED_400),
                    ft.Text(title, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, max_lines=2, size=13),
                    ft.Text("Click to read", size=11, color=ft.Colors.BLUE_200)
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                alignment=ft.alignment.center,
                padding=10,
                on_click=lambda e: page.launch_url(f"{file_name}", web_browser=True), 
                ink=True
            )
        )

    # --- Layout Components ---

    # 1. Header / About Me Section
    about_me_section = ft.Container(
        key="aboutme",
        content=ft.ResponsiveRow([
            ft.Column(
                col={"sm": 12, "md": 7},
                controls=[
                    # FIXED: Swapped TextThemeStyle enums out for native clean string literals
                    ft.Text("About Me", style="headlineLarge", color=PRIMARY_COLOR, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "My name is Aletta Gottlieb, and I am a second-year Electronics and Computer Engineering student. "
                        "During my studies, I participated in a semester project where our team developed an application called BlastMasterPro.\n\n"
                        "In this project, I served as the Project Manager, where I was responsible for coordinating team activities, "
                        "ensuring meetings were conducted as scheduled, and making sure project milestones were completed according to the timeline.\n\n"
                        "The purpose of BlastMasterPro was to assist mining professionals by providing a blasting calculator that simplifies and improves the blasting process.\n\n"
                        "In addition to project management, I have skills in MATLAB, programming, circuit design, and various technical aspects of engineering. "
                        "I am passionate about applying technology and engineering principles to develop practical solutions to real-world problems.",
                        style="bodyLarge"
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Column(
                col={"sm": 12, "md": 5},
                controls=[
                    ft.Container(
                        content=ft.Image(
                            src="zera.JPG",  
                            fit=ft.ImageFit.CONTAIN,
                            border_radius=12,
                        ),
                        alignment=ft.alignment.center,
                        border_radius=12,
                        padding=10,
                    ),
                    ft.Container(height=10),
                    ft.Video(
                        expand=False,
                        playlist=[ft.VideoMedia("alleta.mp4")], 
                        playlist_mode=ft.PlaylistMode.LOOP,
                        fill_color=ft.Colors.BLACK,
                        aspect_ratio=16/9,
                        volume=100,
                        autoplay=False,
                        filter_quality=ft.FilterQuality.HIGH
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]),
        padding=30,
        bgcolor=BG_CARD_COLOR,
        border_radius=16,
        margin=ft.margin.only(bottom=15)
    )

    # 2. Timeline Section
    timeline_section = ft.Container(
        key="timeline",
        content=ft.Column([
            ft.Text("Official Project Timeline", style="headlineMedium", color=PRIMARY_COLOR, weight=ft.FontWeight.BOLD),
            ft.Text("13691CP — 14-Week Semester Layout (02 March – 13 June 2026)", style="bodySmall", italic=True),
            ft.Divider(color=ft.Colors.OUTLINE),
            
            ft.Text("Project Phases Overview", style="titleMedium", weight=ft.FontWeight.BOLD),
            ft.Row([
                ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Phase")),
                        ft.DataColumn(ft.Text("Weeks / Dates")),
                        ft.DataColumn(ft.Text("Core Deliverables & Description")),
                    ],
                    rows=[
                        ft.DataRow(cells=[ft.DataCell(ft.Text("PHASE 0")), ft.DataCell(ft.Text("Wks 1-2 (02–13 Mar)")), ft.DataCell(ft.Text("Group formation, role assignments, GitHub repo setup, environment validation."))]),
                        ft.DataRow(cells=[ft.DataCell(ft.Text("PHASE 1")), ft.DataCell(ft.Text("Wks 3-4 (16–27 Mar)")), ft.DataCell(ft.Text("Pitch Week: Present 3 ideas to Mr. Abisai; official registration."))]),
                        ft.DataRow(cells=[ft.DataCell(ft.Text("PHASE 2")), ft.DataCell(ft.Text("Wks 5-8 (30 Mar–25 Apr)")), ft.DataCell(ft.Text("System Requirements Specification (SRS) document submission (Deadline: 25 Apr)."))]),
                        ft.DataRow(cells=[ft.DataCell(ft.Text("PHASE 3")), ft.DataCell(ft.Text("Wks 9-12 (27 Apr–30 May)")), ft.DataCell(ft.Text("UI/UX interactive high-fidelity prototyping in Figma/Adobe XD (Deadline: 30 May)."))]),
                        ft.DataRow(cells=[ft.DataCell(ft.Text("PHASE 4A")), ft.DataCell(ft.Text("Wk 13 (01–06 Jun)")), ft.DataCell(ft.Text("Live Expo Progress Demonstration running on devices to receive lecturer feedback."))]),
                        ft.DataRow(cells=[ft.DataCell(ft.Text("PHASE 4B")), ft.DataCell(ft.Text("Wk 14 (08–13 Jun)")), ft.DataCell(ft.Text("Final Sprint: Implement feedback, compile APK via EAS Build (Final Deadline: 13 Jun)."))]),
                    ],
                )
            ], scroll=ft.ScrollMode.AUTO),
            
            ft.Container(height=15),
            
            ft.Text("Detailed Weekly Schedule", style="titleMedium", weight=ft.FontWeight.BOLD),
            ft.Row([
                ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Wk")),
                        ft.DataColumn(ft.Text("Dates")),
                        ft.DataColumn(ft.Text("Primary Project Focus Area")),
                    ],
                    rows=[
                        ft.DataRow(cells=[ft.DataCell(ft.Text("1")), ft.DataCell(ft.Text("02–06 Mar")), ft.DataCell(ft.Text("Group formation, roles assigned, create GitHub repo and share URL"))]),
                        ft.DataRow(cells=[ft.DataCell(ft.Text("2")), ft.DataCell(ft.Text("09–13 Mar")), ft.DataCell(ft.Text("Brainstorming 3 ideas; verify Expo + React Native + Firebase environments"))]),
                        ft.DataRow(cells=[ft.DataCell(ft.Text("3")), ft.DataCell(ft.Text("16–20 Mar")), ft.DataCell(ft.Text("Pitch Week Begins: First batch of groups present to Mr. Abisai"))]),
                        ft.DataRow(cells=[ft.DataCell(ft.Text("4")), ft.DataCell(ft.Text("23–27 Mar")), ft.DataCell(ft.Text("Pitch Week Closes: Remaining groups present; register approved app idea"))]),
                        ft.DataRow(cells=[ft.DataCell(ft.Text("5")), ft.DataCell(ft.Text("30 Mar–03 Apr")), ft.DataCell(ft.Text("Begin SRS: Problem statements, target users, scope outlines, overview"))]),
                        ft.DataRow(cells=[ft.DataCell(ft.Text("6")), ft.DataCell(ft.Text("06–10 Apr")), ft.DataCell(ft.Text("SRS Development: Functional requirements (FR) and Firebase collection designs"))]),
                        ft.DataRow(cells=[ft.DataCell(ft.Text("7")), ft.DataCell(ft.Text("13–17 Apr")), ft.DataCell(ft.Text("SRS Development: Non-functional requirements, constraints, use case diagrams"))]),
                        ft.DataRow(cells=[ft.DataCell(ft.Text("8")), ft.DataCell(ft.Text("20–25 Apr")), ft.DataCell(ft.Text("Final edits, SRS verification review, official submission by 25 April 23:59"))]),
                        ft.DataRow(cells=[ft.DataCell(ft.Text("9")), ft.DataCell(ft.Text("27 Apr–01 May")), ft.DataCell(ft.Text("Figma design start: Onboarding views, splash screens, main structural layouts"))]),
                        ft.DataRow(cells=[ft.DataCell(ft.Text("10")), ft.DataCell(ft.Text("04–08 May")), ft.DataCell(ft.Text("Figma design: Core interactive app screens, data fields, forms, lists"))]),
                        ft.DataRow(cells=[ft.DataCell(ft.Text("11")), ft.DataCell(ft.Text("11–15 May")), ft.DataCell(ft.Text("Figma layout completion: Interactive wireframe linking and design rationale draft"))]),
                        ft.DataRow(cells=[ft.DataCell(ft.Text("12")), ft.DataCell(ft.Text("18–30 May")), ft.DataCell(ft.Text("Prototype tracking refinements, presentation, official submission by 30 May 23:59"))]),
                        ft.DataRow(cells=[ft.DataCell(ft.Text("13")), ft.DataCell(ft.Text("01–06 Jun")), ft.DataCell(ft.Text("Live Progress Demo: Present active Expo Go app to Mr. Abisai for critiques"))]),
                        ft.DataRow(cells=[ft.DataCell(ft.Text("14")), ft.DataCell(ft.Text("08–13 Jun")), ft.DataCell(ft.Text("Final Sprint: Cloud EAS build for standalone APK; complete documentation packages"))]),
                    ],
                )
            ], scroll=ft.ScrollMode.AUTO)
        ]),
        padding=20,
        bgcolor=BG_CARD_COLOR,
        border_radius=16,
        margin=ft.margin.only(bottom=15)
    )

    # 3. Technical Blog Section
    blog_section = ft.Container(
        key="blog",
        content=ft.Column([
            ft.Text("Technical Blog / Engineering Logs", style="headlineMedium", color=PRIMARY_COLOR, weight=ft.FontWeight.BOLD),
            ft.Divider(color=ft.Colors.OUTLINE),
            ft.ListTile(
                leading=ft.Icon(ft.icons.ARTICLE),
                title=ft.Text("Mastering Flet UI Layouts"),
                subtitle=ft.Text("Deep dive into building responsive architectures using Python structures..."),
            ),
            ft.ListTile(
                leading=ft.Icon(ft.icons.ARTICLE),
                title=ft.Text("Understanding Vector Calculus in System Models"),
                subtitle=ft.Text("Analyzing matrices and spatial gradients for engineering setups..."),
            ),
        ]),
        padding=20,
        bgcolor=BG_CARD_COLOR,
        border_radius=16,
        margin=ft.margin.only(bottom=15)
    )

    # 4. Matlab Achievement Hub Section
    matlab_section = ft.Container(
        key="matlab",
        content=ft.Column([
            ft.Text("Matlab Achievement Hub", style="headlineMedium", color=PRIMARY_COLOR, weight=ft.FontWeight.BOLD),
            ft.Divider(color=ft.Colors.OUTLINE),
            ft.Text("Engineering app instances, RLC parallel resonance analysis profiles, and Simulink control layouts module representations live here.", style="bodyMedium"),
            ft.Container(height=5),
            ft.GridView(
                expand=False,
                runs_count=4,
                max_extent=180,
                child_aspect_ratio=0.95,
                spacing=15,
                run_spacing=15,
                controls=[
                    create_certificate_card("MATLAB Onramp", "certificate1.pdf"),
                    create_certificate_card("Simulink Onramp", "certificate2.pdf"),
                    create_certificate_card("Explore Plots", "certificate3.pdf"),
                    create_certificate_card("Manipulate Matrices", "certificate4.pdf"),
                    create_certificate_card("Vectors & Matrices", "certificate5.pdf"),
                    create_certificate_card("Circuit Simulation", "certificate6.pdf"),
                    create_certificate_card("Matrix Calculations", "certificate7.pdf"),
                    create_certificate_card("Writing Functions", "certificate8.pdf"),
                ]
            )
        ]),
        padding=20,
        bgcolor=BG_CARD_COLOR,
        border_radius=16,
        margin=ft.margin.only(bottom=15)
    )

    # 5. Commit History Section
    commit_section = ft.Container(
        key="commit",
        content=ft.Column([
            ft.Text("Commit History", style="headlineMedium", color=PRIMARY_COLOR, weight=ft.FontWeight.BOLD),
            ft.Divider(color=ft.Colors.OUTLINE),
            ft.Text("Latest snapshot of the active GitHub ecosystem branch:", style="bodyMedium"),
            ft.Container(height=10),
            ft.Image(
                src="commit_history.png",  
                fit=ft.ImageFit.CONTAIN,
                border_radius=8,
            )
        ]),
        padding=20,
        bgcolor=BG_CARD_COLOR,
        border_radius=16,
        margin=ft.margin.only(bottom=15)
    )

    # 6. Pull Request Logs Section
    pr_section = ft.Container(
        key="pr",
        content=ft.Column([
            ft.Text("Pull Request Logs", style="headlineMedium", color=PRIMARY_COLOR, weight=ft.FontWeight.BOLD),
            ft.Divider(color=ft.Colors.OUTLINE),
            ft.Row([
                ft.Icon(ft.icons.MERGE_TYPE, color=ft.Colors.PURPLE_400),
                ft.Text("PR #12: Merged Phase 2 SRS functional models into documentation main branch", style="bodyMedium")
            ]),
            ft.Row([
                ft.Icon(ft.icons.MERGE_TYPE, color=ft.Colors.PURPLE_400),
                ft.Text("PR #11: Implemented foundational Expo configuration files and initial dependencies", style="bodyMedium")
            ]),
            ft.Container(height=10),
            ft.ElevatedButton(
                text="View on GitHub",
                icon=ft.icons.LAUNCH,
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.BLUE_600,
                on_click=open_github
            )
        ]),
        padding=20,
        bgcolor=BG_CARD_COLOR,
        border_radius=16,
        margin=ft.margin.only(bottom=150)
    )

    # --- Application Shell Configuration ---
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.icons.MENU, on_click=handle_menu_click),
        leading_width=40,
        title=ft.Row([
            ft.CircleAvatar(
                foreground_image_url="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe",
                radius=16
            ),
            ft.Text("Welcome To My Portfolio", weight=ft.FontWeight.W_500)
        ], spacing=10),
        center_title=False,
        bgcolor=ft.Colors.SURFACE,
        actions=[
            ft.IconButton(ft.icons.ADMIN_PANEL_SETTINGS_OUTLINED, on_click=handle_admin_click, tooltip="take me to admin_console"),
        ],
    )

    page.drawer = ft.NavigationDrawer(
        on_change=handle_drawer_change,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(label="Home", icon=ft.icons.HOME),
            ft.NavigationDrawerDestination(label="Timeline", icon=ft.icons.CALENDAR_MONTH),
            ft.NavigationDrawerDestination(label="Engineering logs", icon=ft.icons.BOOKMARK_BORDER),
            ft.NavigationDrawerDestination(label="Matlab hub", icon=ft.icons.ASSESSMENT),
            ft.NavigationDrawerDestination(label="Commit history", icon=ft.icons.HISTORY),
            ft.NavigationDrawerDestination(label="Pull request logs", icon=ft.icons.MERGE_TYPE),
        ]
    )

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.CHAT_BUBBLE_ROUNDED,
        bgcolor=PRIMARY_COLOR,
        on_click=handle_message_click,
        tooltip="messages"
    )

    page.add(
        ft.SafeArea(
            ft.Container(
                content=ft.Column([
                    about_me_section,
                    timeline_section,
                    blog_section,
                    matlab_section,
                    commit_section,
                    pr_section
                ], spacing=10),
                padding=10
            )
        )
    )

# --- AUTOMATED WEB PATCH FOR WEBHINT ERRORS ---
def apply_webhint_patch():
    """Finds the exported web layout and injects compliance variables."""
    web_dir = os.path.join(os.path.dirname(__file__), "web")
    index_html = os.path.join(web_dir, "index.html")
    if os.path.exists(index_html):
        with open(index_html, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace restricted scaling viewports with adaptive accessible headers
        bad_meta = 'content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"'
        good_meta = 'content="width=device-width, initial-scale=1.0, initial-scale=1.0"'
        
        if bad_meta in content:
            content = content.replace(bad_meta, good_meta)
            with open(index_html, "w", encoding="utf-8") as f:
                f.write(content)
            print("[System] Webhint accessibility validation patch successfully injected.")

if __name__ == "__main__":
    import sys
    # Runs compilation pipeline
    ft.app(target=main, assets_dir="assets")
    
    # Executes HTML cleanup rule right after build generation completes
    if "export" in sys.argv or "--web" in sys.argv:
        apply_webhint_patch()
