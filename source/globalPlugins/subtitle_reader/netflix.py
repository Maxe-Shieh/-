#coding=utf-8

from .subtitle_alg import SubtitleAlg
from .object_finder import find

class Netflix(SubtitleAlg):
	def getVideoPlayer(self):
		obj = self.main.focusObject
		return find(obj, 'parent', 'role', 52)
	
	def getSubtitleContainer(self):
		videoPlayer = self.main.videoPlayer
		appName = videoPlayer.appModule.appName
		return getattr(self, appName + 'GetSubtitleContainer')()
	
	def chromeGetSubtitleContainer(self):
		obj = self.main.videoPlayer
		obj = find(obj, 'firstChild', 'role', 56)
		return obj
	
	def firefoxGetSubtitleContainer(self):
		obj = self.main.videoPlayer
		obj = find(obj, 'firstChild', 'role', 56)
		return obj
	
	def getSubtitle(self):
		subtitle = ''
		obj = self.main.subtitleContainer
		obj = obj.next
		while obj and not obj.name:
			try:
				obj = obj.firstChild
			except:
				obj = None
			
		
		while obj:
			if obj.name:
				subtitle += obj.name + '\r\n'
			
			obj = obj.next
		
		return subtitle
	
