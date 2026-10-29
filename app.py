                        <div class='card-inner-clearance'>
                            <div style='display:flex; justify-content:space-between; align-items:center;'>
                                <div class='card-title' style='margin-bottom:0;'>{wj['Request ID']} | Station: {wj['Station Location']} | Group: {wj['Combined Group ID']}</div>
                                <span style='font-size:10px; font-weight:800; color:white; background:{p_color}; padding:2px 8px; border-radius:6px; letter-spacing:0.4px;'>{p_badge}</span>
                            </div>
                            <div style='font-size: 15px; font-weight:800; color:#0F172A; margin-top:4px;'>{wj['Work Description']}</div>
                            <div style='font-size: 12px; color:#334155; margin-top: 4px;'>
                                <b>Duration:</b> {wj['Duration (Minutes)']} Minutes | <b>Machine:</b> {wj['Assigned Machinery']} | <b>Priority Level:</b> <span style="font-weight:bold; color:{p_color};">{wj['Priority Level (1-100)']}/100</span>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("No weekly tasks scheduled for this department.")

        with f_tabs[2]:
            st.markdown("#### Upcoming 30-Day Tasks")
            monthly_jobs = filtered_block_reqs[filtered_block_reqs["Planning Schedule"] == "Monthly Plan (Next 30 Days)"]
            if not monthly_jobs.empty:
                for _, mj in monthly_jobs.iterrows():
                    card_css, p_color, p_badge = get_priority_card_class(mj["Priority Level (1-100)"], mj["Work Description"])
                    st.markdown(f"""
                    <div class='{card_css}'>
                        <div class='card-inner-clearance'>
                            <div style='display:flex; justify-content:space-between; align-items:center;'>
                                <div class='card-title' style='margin-bottom:0;'>{mj['Request ID']} | Station: {mj['Station Location']} | Group: {mj['Combined Group ID']}</div>
                                <span style='font-size:10px; font-weight:800; color:white; background:{p_color}; padding:2px 8px; border-radius:6px; letter-spacing:0.4px;'>{p_badge}</span>
                            </div>
                            <div style='font-size: 15px; font-weight:800; color:#0F172A; margin-top:4px;'>{mj['Work Description']}</div>
                            <div style='font-size: 12px; color:#334155; margin-top: 4px;'>
                                <b>Duration:</b> {mj['Duration (Minutes)']} Minutes | <b>Machine:</b> {mj['Assigned Machinery']} | <b>Priority Level:</b> <span style="font-weight:bold; color:{p_color};">{mj['Priority Level (1-100)']}/100</span>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("No monthly tasks scheduled for this department.")
