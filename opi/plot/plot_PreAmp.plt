<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<databrowser>
    <title></title>
    <save_changes>true</save_changes>
    <show_legend>false</show_legend>
    <show_toolbar>true</show_toolbar>
    <grid>false</grid>
    <scroll>true</scroll>
    <update_period>3.0</update_period>
    <scroll_step>5</scroll_step>
    <start>-5 minutes 0.0 seconds</start>
    <end>now</end>
    <archive_rescale>NONE</archive_rescale>
    <foreground>
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
    </foreground>
    <background>
        <red>230</red>
        <green>235</green>
        <blue>232</blue>
    </background>
    <title_font>Liberation Sans|20|1</title_font>
    <label_font>Liberation Sans|14|1</label_font>
    <scale_font>Liberation Sans|12|0</scale_font>
    <legend_font>Liberation Sans|14|0</legend_font>
    <axes>
        <axis>
            <visible>true</visible>
            <name>Value 1</name>
            <use_axis_name>false</use_axis_name>
            <use_trace_names>true</use_trace_names>
            <right>false</right>
            <color>
                <red>0</red>
                <green>0</green>
                <blue>0</blue>
            </color>
            <min>-0.238</min>
            <max>4.997999999999999</max>
            <grid>false</grid>
            <autoscale>true</autoscale>
            <log_scale>false</log_scale>
        </axis>
    </axes>
    <annotations>
    </annotations>
    <pvlist>
        <pv>
            <display_name>PreAmp Fwd</display_name>
            <visible>true</visible>
            <name>$(SYSTEM):AI$(chPreAmp)-SMON-MAGCURR</name>
            <axis>0</axis>
            <color>
                <red>47</red>
                <green>135</green>
                <blue>147</blue>
            </color>
            <trace_type>AREA</trace_type>
            <linewidth>2</linewidth>
            <line_style>SOLID</line_style>
            <point_type>NONE</point_type>
            <point_size>2</point_size>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>RAW</request>
        </pv>
    </pvlist>
</databrowser>