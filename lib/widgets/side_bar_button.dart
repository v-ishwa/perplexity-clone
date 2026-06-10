import 'package:flutter/material.dart';
import 'package:perplexity_clone/theme/colors.dart';

class SideBarButton extends StatefulWidget {
  final bool isCollapsed;
  final IconData icon;
  final String text;
  const SideBarButton({
    required this.isCollapsed,
    required this.icon,
    required this.text,
    super.key,
  });

  @override
  State<SideBarButton> createState() => _SideBarButtonState();
}

class _SideBarButtonState extends State<SideBarButton> {
  bool isHovering = false;
  @override
  Widget build(BuildContext context) {
    return MouseRegion(
      onEnter: (event) {
        setState(() {
          isHovering = true;
        });
      },
      onExit: (event) {
        setState(() {
          isHovering = false;
        });
      },
      child: Container(
        decoration: BoxDecoration(
          color: isHovering ? AppColors.proButton : Colors.transparent,
          borderRadius: BorderRadius.circular(6),
        ),
        child: Row(
          mainAxisAlignment: widget.isCollapsed
              ? MainAxisAlignment.center
              : MainAxisAlignment.start,
          children: [
            Container(
              margin: EdgeInsets.symmetric(vertical: 14, horizontal: 10),
              child: Icon(widget.icon, color: AppColors.iconGrey, size: 22),
            ),
            SizedBox(width: widget.isCollapsed ? 0 : 10),
            widget.isCollapsed
                ? const SizedBox(width: 0, height: 0)
                : Text(
                    widget.text,
                    style: TextStyle(
                      color: AppColors.textGrey,
                      fontSize: 16,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
          ],
        ),
      ),
    );
  }
}
